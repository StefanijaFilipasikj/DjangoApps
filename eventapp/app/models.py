from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Band(models.Model):
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    year_of_forming = models.IntegerField()
    num_events = models.IntegerField()

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateTimeField()
    poster = models.ImageField(upload_to='photos/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    open = models.BooleanField()
    bands = models.CharField(max_length=255, null=True, blank=True)
    number_of_bands = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class BandInEvent(models.Model):
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.band.name} - {self.event.name}'

    def save(self, *args, **kwargs):
        band = self.band
        event = self.event
        band.num_events += 1
        band.save()
        event.number_of_bands += 1
        event.save()
        super(BandInEvent, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        band = self.band
        band.num_events -= 1
        band.save()
        event = self.event
        event.number_of_bands -= 1
        event.save()
        super(BandInEvent, self).delete(*args, **kwargs)
