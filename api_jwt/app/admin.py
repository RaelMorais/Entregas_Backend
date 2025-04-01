from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario


class UsuarioAdmin(UserAdmin):
    
    list_display = ('username', 'email', 'data_nascimento', 'idade', 'biografia',  'telefone', 'escolaridade', 'rua', 'numero', 'cidade', 'estado', 'cep', 'pais','nome_animal' ,'especie_animal','qtd_animais') 
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields':('data_nascimento', 'idade', 'biografia', 'telefone', 'escolaridade', 'rua', 'numero', 'cidade', 'estado', 'cep', 'pais','nome_animal' ,'especie_animal','qtd_animais')}), 

    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('data_nascimento', 'idade', 'biografia', 'telefone', 'escolaridade', 'rua', 'numero', 'cidade', 'estado', 'cep', 'pais','nome_animal' ,'especie_animal','qtd_animais')}), 
    )

admin.site.register(Usuario, UsuarioAdmin)
# Register your models here.
