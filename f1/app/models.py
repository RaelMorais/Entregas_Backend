from django.db import models

times = (
        ("Apn", "Alpine"),
        ("Wls", "Williams"),
        ("Frr", "Ferrari"),
        ("Hss", "Hass"),
        ("Amg", "Mercedes"),
        ("Rbr", "Red Bull"),
        ("Vrb", "Racing Bulls"),
        ("Sbr", "Sauber"),
        ("Mcl", "McLaren"),
        ("AsM", "Aston Martin"),
    )



class Carro(models.Model):
    nome = models.CharField(max_length=255)
    marca = models.CharField(max_length=255)
    velo_max = models.CharField(max_length=255)

    def __str__(self):
        return self.nome
class Piloto (models.Model):
    nome = models.CharField(max_length=255)
    idade = models.CharField(max_length=255)
    classificacao = models.CharField(max_length=255)
    time = models.CharField(choices=times, max_length=10)

    def __str__(self):
        return self.nome

   
# Create your models here.
