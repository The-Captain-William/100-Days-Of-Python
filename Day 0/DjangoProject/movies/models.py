from django.db import models
from django.utils import timezone

# Create your models here.


class Genre(models.Model):  # inherit from Model class
    name = models.CharField(max_length=255)  # limit length to prevent hacker griefing
    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    number_in_stock = models.IntegerField()
    daily_rate = models.FloatField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)  # cascade prevents genre deletion from deleting all films
    date_created = models.DateTimeField(default=timezone.now)  # dont add () to timezone.now or you will hardcode
    def __str__(self):
        return  self.title