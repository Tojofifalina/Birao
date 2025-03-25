from django.db import models

# Create your models here.
class VolaNiditra(models.Model):
    Taona = models.PositiveIntegerField()
    Daty = models.DateField()
    Antony = models.CharField(max_length=250)
    Vola = models.PositiveIntegerField()
    Fanamarihana = models.TextField(900)

class VolaNivoka(models.Model):
    Taona = models.PositiveIntegerField()
    Daty = models.DateField()
    Antony = models.CharField(max_length=250)
    Vola = models.PositiveIntegerField()
    Fanamarihana = models.TextField(900)