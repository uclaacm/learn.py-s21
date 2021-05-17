from django.db import models

# Create your models here.
class FlyerPerson(models.Model):
    name = models.CharField(max_length=100)
    pitch = models.TextField()
    flyers_given = models.IntegerField()
