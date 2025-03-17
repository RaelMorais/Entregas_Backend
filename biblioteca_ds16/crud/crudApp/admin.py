
from django.contrib import admin
from .models import Livros, Autor, Genero

admin.site.register(Autor)
admin.site.register(Livros)
admin.site.register(Genero)


# Register your models here.
