from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length= 100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length= 200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name= "books")

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




    

