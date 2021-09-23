from django.db import models

# Create your models here.

#Modelo para la entidad Autor. 
class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)

#Modelo para la entidad Categoría
class Category(models.Model):
    name = models.CharField(max_length=30)

#Modelo para la entidad Libros
class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=500)