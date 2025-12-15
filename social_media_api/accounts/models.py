from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    """
    Custom User model for the Social Media API.

    Fields:
    - bio: Short user biography
    - profile_picture: Optional profile image
    - followers: Users who follow this user
    """

    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(
        upload_to="profile_pictures/",
        blank=True,
        null=True
    )

    followers = models.ManyToManyField(
        "self",
        symmetrical=False,
        related_name="following",
        blank=True
    )

    def __str__(self):
        return self.username
