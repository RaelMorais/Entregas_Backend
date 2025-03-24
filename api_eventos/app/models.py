from django.db import models

class Place(models.Model):
    name_place = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=10)
    coutry = models.CharField(max_length=255)
    neighborhood = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)

    def __str__(self):
        return self.name_place  

class Category(models.Model):
    name_category = models.CharField(max_length=255)

    def __str__(self):
        return self.name_category

class Event(models.Model):
    name = models.CharField(max_length=255)
    date_init = models.DateField()
    date_end = models.DateField()
    hour_init = models.TimeField(null=True)
    hour_end = models.TimeField(null=True)
    location = models.ForeignKey(Place, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default="0")


    def __str__(self):
        return self.name
    
class Client(models.Model):
    name = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=255)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    


# Create your models here.
