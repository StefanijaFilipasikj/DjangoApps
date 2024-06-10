from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Manufacturer(models.Model):
    name = models.CharField(max_length=30)
    url = models.CharField(max_length=120)
    country_of_origin = models.CharField(max_length=30)
    owner_name = models.CharField(max_length=30)


class Automobile(models.Model):
    type = models.CharField(max_length=10)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    max_speed = models.IntegerField()
    color = models.CharField(max_length=10)


class RepairShop(models.Model):
    name = models.CharField(max_length=30)
    year_of_funding = models.IntegerField()
    old_timer = models.BooleanField()


class Repair(models.Model):
    code = models.CharField(max_length=30)
    date = models.DateField()
    problem_desc = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/', blank=True, null=True)
    automobile = models.ForeignKey(Automobile, on_delete=models.CASCADE)
    shop = models.ForeignKey(RepairShop, on_delete=models.CASCADE)


class RepairShopManufacturer(models.Model):
    shop = models.ForeignKey(RepairShop, on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)