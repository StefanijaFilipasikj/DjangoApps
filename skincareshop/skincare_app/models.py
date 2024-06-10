from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=30)
    continent = models.CharField(max_length=3, choices=[('AS', 'Asia'), ('EU', 'Europe'), ('AF', 'Africa'), ('NL', 'North America'), ('SA', 'South America'), ('AU', 'Australia')])

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=30)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    founded = models.DateField()
    email = models.EmailField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos/')
    price = models.DecimalField(max_digits=7, decimal_places=2)
    category = models.CharField(max_length=3, choices=[('CL', 'Cleanser'), ('MR', 'Moisturizer'), ('TN', 'Toner'),('SR', 'Serum'), ('SN', 'Sunscreen'), ('MS', 'Mask')])
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    release_date = models.DateTimeField()

    def __str__(self):
        return f'{self.brand.name} {self.name}'


class StoreLocation(models.Model):
    name = models.CharField(max_length=30)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    global_delivery = models.BooleanField()

    def __str__(self):
        return self.name


class ProductInStore(models.Model):
    location = models.ForeignKey(StoreLocation, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    in_stock = models.IntegerField()
