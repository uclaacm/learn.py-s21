from django.db import models

# Create your models here.

class FlyerPerson(models.Model):
    name = models.CharField(max_length=128)
    pitch = models.CharField(max_length=128)
    flyers_given = models.IntegerField(default=0)
