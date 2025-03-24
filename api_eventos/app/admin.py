from django.contrib import admin
from .models import Event, Client, Place, Category

admin.site.register(Place)
admin.site.register(Event)
admin.site.register(Category)
admin.site.register(Client)

# Register your models here.
