from django.db import models
from django.contrib.postgres.fields import ArrayField

from django.contrib.auth.models import AbstractUser
from django.db.models.base import Model

# Create your models here.
class CustomUser(AbstractUser):
    # Any extra fields would go here
    def __str__(self):
        return self.email


class Region(models.Model):
    class RegionType(models.TextChoices):
        WTR = "water","water"
        WOD = "woodland","woodland"
        MTN = "mountain","mountain"
        PLN = "plain","plain"
    
    type = models.CharField(max_length=10,choices=RegionType.choices)
    class RegionDevelopment(models.TextChoices):
        WILDS = "wilds","wilds"
        UNDEV = "undev","undev"
        RURAL = "rural","rural"
        SUBUR = "suburbs","suburbs"
        SEMIU = "semiurban","semiurban"
        URBAN = "urban","urban"
        METRO = "metropolis","metropolis"
    development = models.CharField(max_length=10,choices=RegionDevelopment.choices)
    rich_soil = models.BooleanField(max_length=10,default=False)
    rich_coal = models.BooleanField(max_length=10,default=False)
    rich_oilfield = models.BooleanField(max_length=10,default=False)
    rich_uranium = models.BooleanField(max_length=10,default=False)
    rich_rareearth = models.BooleanField(max_length=10,default=False)
    rich_metals = models.BooleanField(max_length=10,default=False)
    

class GameWorld(models.Model):
    name = models.CharField(max_length=50)
