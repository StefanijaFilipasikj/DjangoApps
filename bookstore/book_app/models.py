from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class PublishingHouse(models.Model):
    name = models.CharField(max_length=30)
    founding_year = models.IntegerField()
    website = models.URLField()

    address = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='photos/')
    isbn = models.CharField(max_length=13, unique=True)
    year_of_publishing = models.IntegerField()
    publishing_house = models.ForeignKey('PublishingHouse', on_delete=models.CASCADE)
    num_pages = models.IntegerField()
    dimensions = models.CharField(max_length=10)
    book_cover_type = models.CharField(max_length=3, choices = [('SF', 'Soft'), ('HR', 'Hard')])
    category = models.CharField(max_length=3, choices = [('RM', 'Romance'), ('TH', 'Thriller'), ('BI', 'Biography'), ('CL', 'Classic'), ('DR', 'Drama'), ('HR', 'Historical')])
    price = models.DecimalField(max_digits=7, decimal_places=3)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name} {self.surname}'


class BookAuthor(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    type = models.CharField(max_length=2, choices=[('M', 'Main'), ('S', 'Secondary')])


class PublishingHouseAuthor(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    publishing_house = models.ForeignKey('PublishingHouse', on_delete=models.CASCADE)
    years = models.IntegerField()