from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Balloon(models.Model):
    type = models.CharField(max_length=30)
    manufacturer = models.CharField(max_length=50)
    max_capacity = models.IntegerField()

    def __str__(self):
        return self.type


class Airline(models.Model):
    name = models.CharField(max_length=30)
    founding_year = models.IntegerField()
    outside_europe = models.BooleanField()

    def __str__(self):
        return self.name


class Pilot(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    birth_year = models.IntegerField()
    total_hours = models.IntegerField()
    position = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class BalloonFlight(models.Model):
    code = models.CharField(max_length=30)
    from_airport = models.CharField(max_length=50, blank=True, null=True)
    to_airport = models.CharField(max_length=50, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    balloon = models.ForeignKey(Balloon, on_delete=models.CASCADE)
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE)
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)

    def __str__(self):
        return self.code


class AirlinePilot(models.Model):
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.airline} - {self.pilot}'
