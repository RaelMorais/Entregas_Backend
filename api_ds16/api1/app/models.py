from django.db import models


class Car(models.Model):
    name_car = models.CharField(max_length=255)
    name_factory = models.CharField(max_length=255)
    horsepower = models.FloatField()
    category = models.CharField(max_length=255)
    qty_ports = models.PositiveIntegerField()
    qty_roads = models.PositiveIntegerField()
    color = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    choice_fuel = (
        ('gs', 'Gasoline'),
        ('gnv', 'Compressed Natural Gas'),
        ('al', 'Ethanol'),
        ('ev', 'Electric'),
        ('ds', 'Diesel'),
        ('bd', 'Biodiesel'),
        ('bs', 'Biofuel'), 
    )
    fuel = models.CharField(max_length=9, choices=choice_fuel)

    def __str__(self):
        return "Deu certo!"
# Create your models here.
