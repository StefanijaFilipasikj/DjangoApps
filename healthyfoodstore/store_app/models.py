from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    active = models.BooleanField()

    def __str__(self):
        return self.name


class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    client_email = models.EmailField()

    def __str__(self):
        return f'{self.name} {self.surname}'


class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):
    date = models.DateField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)


class ProductInOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField()
