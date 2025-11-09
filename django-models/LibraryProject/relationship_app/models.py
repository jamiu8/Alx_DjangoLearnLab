from django.db import models

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
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
         return f"{self.librarian_name} in {self.library}"

    

