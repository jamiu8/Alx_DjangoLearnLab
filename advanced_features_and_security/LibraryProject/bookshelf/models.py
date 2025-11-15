from django.db import models
from django.contrib.auth.models import User, AbstractUser, BaseUserManager
from django.contrib.auth.backends import BaseBackend

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length= 200)
    author = models.CharField(max_length= 100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"Books are {self.title} by {self.author} realeased in {self.publication_year}"
    
    class CustomUserManager(BaseUserManager):
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

class CustomUser(AbstractUser):
    username = models.CharField(max_length= 100)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    profile_photo = models.ImageField(upload_to='profile_pics/', blank=True, null=True)