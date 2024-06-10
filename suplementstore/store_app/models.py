from django.contrib.auth.models import User
from django.db import models
# Create your models here.


class Manufacturer(models.Model):
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class NutritionalValue(models.Model):
    calories = models.IntegerField()
    proteins = models.IntegerField()
    carbohydrates = models.IntegerField()
    fats = models.IntegerField()

    def __str__(self):
        return f'cal: {self.calories}, pt: {self.proteins}, cb: {self.carbohydrates}, ft: {self.fats}'


class Supplement(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='photos/')
    code = models.CharField(max_length=10)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    available = models.BooleanField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    category = models.CharField(max_length=3, choices=[('PR', 'proteins'), ('VT', 'vitamins'), ('CR', 'creatines'), ('AA', 'amino acids'), ('PW', 'pre-workout')])
    nutritional_value = models.ForeignKey(NutritionalValue, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ActiveIngredient(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ActiveIngredientInSupplement(models.Model):
    supplement = models.ForeignKey(Supplement, on_delete=models.CASCADE)
    active_ingredient = models.ForeignKey(ActiveIngredient, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
