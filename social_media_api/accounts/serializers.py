from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model
from rest_framework.authtoken.models import Token

# Get the active User model (custom or default)
User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Handles user registration using Django's recommended
    get_user_model().objects.create_user approach.
    """

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password", "bio"]

    def create(self, validated_data):
        """
        Create a new user and automatically generate an auth token.
        """

        user = get_user_model().objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email"),
            password=validated_data["password"],
            bio=validated_data.get("bio", "")
        )

        # Create authentication token
        Token.objects.create(user=user)

        return user


class UserLoginSerializer(serializers.Serializer):
    """
    Authenticates user credentials and returns token.
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
            "user": user.username,
            "token": token.key
        }


class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializes user profile data.
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
