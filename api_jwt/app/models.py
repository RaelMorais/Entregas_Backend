from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    """
    Modelo de usuário personalizado, que herda de AbstractUser e adiciona campos personalizados.
    """
    # Informações pessoais 
    data_nascimento = models.DateField()
    idade = models.PositiveIntegerField()
    biografia = models.TextField(max_length=255, null=True, blank=True)
    telefone = models.CharField(max_length=255, null=True, blank=True)
    escolaridade = models.CharField(max_length=255, null=True, blank=True)
    
    # Informações onde mora 
    rua = models.CharField(max_length=255)
    numero = models.CharField(max_length=10, null=True, blank=True)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    cep = models.CharField(max_length=255)
    pais = models.CharField(max_length=255)

    # Informações animais 
    nome_animal = models.CharField(max_length=255, null=True, blank=True)
    especie_animal = models.CharField(max_length=255, null=True, blank=True) 
    qtd_animais = models.PositiveIntegerField(null=True, blank=True)  # Quantidade de animais (não é mais FK)

    REQUIRED_FIELDS = ['data_nascimento', 'idade', 'rua', 'cidade', 'estado', 'cep', 'pais']

    def __str__(self):
        return self.username

