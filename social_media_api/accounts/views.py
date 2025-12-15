from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from .models import User
from .serializers import (
    UserRegistrationSerializer,
    UserLoginSerializer,
    UserProfileSerializer
)

# Create your views here.

class RegisterView(generics.CreateAPIView):
    """
    User registration endpoint.
    Returns authentication token on success.
    """
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer


class LoginView(generics.GenericAPIView):
    """
    User login endpoint.
    Returns authentication token.
    """
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class ProfileView(generics.RetrieveUpdateAPIView):
    """
    Retrieve and update authenticated user's profile.
    """
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
