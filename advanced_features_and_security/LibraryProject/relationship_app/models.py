from typing import Any
from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.backends import BaseBackend
from django.http import HttpRequest

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length= 100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length= 200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name= "books")

    class Meta:
        permissions = (
            ("can_add_book", "Can add a book"),
            ("can_change_book", "Can change a book"),
            ("can_delete_book", "Can delete a book"),
        )

    def __str__(self):
        return f"{self.title} by {self.author}"

class Library(models.Model):
    library_name = models.CharField(max_length= 100)
    books = models.ManyToManyField(Book)

    def __str__(self):
         return f"{self.books} in {self.library_name}"
class Librarian(models.Model):
    librarian_name = models.CharField(max_length= 100)
    library_name = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
         return f"{self.librarian_name} in {self.library_name}"
    
class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} ({self.role})"

# Signal to automatically create a UserProfile when a User is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

class CustomUserManger(BaseUserManager):
    def create_user(self, email, password = None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length= 100)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    profile_photo = models.ImageField(upload_to='profile_pics/', blank=True, null=True)


'''class AuthBack(BaseBackend):
    def authenticate(self, request: HttpRequest, username: str | None = ..., password: str | None = ..., **kwargs: Any) -> AbstractBaseUser | None:
        return super().authenticate(request, username, password, **kwargs)
    
    def get_user(self, user_id: int) -> AbstractBaseUser | None:
        return super().get_user(user_id)
'''


    

