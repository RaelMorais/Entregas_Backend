from django.contrib import admin
from .models import Event, Client, Place, Category

#Definição de permissão para adicionar itens no site de Admin, é usado apenas para testes iniciais do Banco. 
admin.site.register(Place)
admin.site.register(Event)
admin.site.register(Category)
admin.site.register(Client)

# Register your models here.
