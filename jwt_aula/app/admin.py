from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UsuarioDS16

class UsuarioDS16Admin(UserAdmin):
    """
    Personaliza o painel de administração para o modelo UsuarioDS16, 
    permitindo a exibição e edição dos campos adicionais (data_nascimento, edv, padrinho, apelido) 
    diretamente na interface do Django Admin.
    """
    
    list_display = ('username', 'email', 'data_nascimento', 'edv', 'padrinho', 'apelido') # 'list_display' define os campos que serão exibidos na lista de usuários do painel de administração.
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields':('data_nascimento', 'edv', 'padrinho', 'apelido')}), # 'fieldsets' define como os campos de um usuário serão organizados nas telas de edição.

    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('data_nascimento', 'edv', 'padrinho', 'apelido')}), # 'add_fieldsets' define os campos a serem exibidos quando um novo usuário é criado no painel de administração.
    )

admin.site.register(UsuarioDS16, UsuarioDS16Admin) # O modelo 'UsuarioDS16' é registrado no Django Admin com a classe personalizada 'UsuarioDS16Admin',

# Register your models here.
