from django.db import models

# Create your models here.
class GridData(models.Model):
    latitude_start = models.FloatField()
    latitude_end = models.FloatField()
    longitude_start = models.FloatField()
    longitude_end = models.FloatField()
    height_start = models.FloatField()
    height_end = models.FloatField()

class GridPoint(models.Model):
    grid_data = models.ForeignKey(GridData, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    value = models.FloatField()
