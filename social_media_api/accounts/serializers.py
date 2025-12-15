from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Handles user registration and token creation.
    """

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password", "bio"]

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email"),
            password=validated_data["password"],
            bio=validated_data.get("bio", "")
        )
        Token.objects.create(user=user)
        return user


class UserLoginSerializer(serializers.Serializer):
    """
    Handles user authentication and token retrieval.
    """

    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(
            username=data["username"],
            password=data["password"]
        )

        if not user:
            raise serializers.ValidationError("Invalid credentials")

        token, created = Token.objects.get_or_create(user=user)

        return {
            "user": user,
            "token": token.key
        }


class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializes user profile information.
    """

    followers_count = serializers.IntegerField(
        source="followers.count",
        read_only=True
    )

    following_count = serializers.IntegerField(
        source="following.count",
        read_only=True
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "bio",
            "profile_picture",
            "followers_count",
            "following_count",
        ]
