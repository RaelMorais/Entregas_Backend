from django.contrib import admin
from .models import Car

admin.site.register(Car) #Chamando o modelo do nosso Banco para poder registrar os dados pelo Site "admin"
# Register your models here.
