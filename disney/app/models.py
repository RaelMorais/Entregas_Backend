from django.db import models
from django.contrib.auth.models import AbstractUser



class Empresa(models.Model):
    nome_fantasia = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=100)

class Usuario(AbstractUser):
    apelido = models.CharField(max_length=100, null=True, blank=True)
    telefone = models.CharField(max_length=100, null=True, blank=True)
    genero = models.CharField(max_length=100, choices=(('M', 'Masculino'), ('F', 'Feminino'), ('N','Neutro')), null=True, blank=True)

    escolha_funcao = (
        ('G','Gestor'),
        ('C', 'Colaborador'),
        ('A', 'Aprendiz'),
        ('E', 'Estágio'), 
        ('M', 'Meio-Oficial')
    )

    colaborador = models.CharField(max_length=1, choices=escolha_funcao, default='C')


    REQUIRED_FIELDS = ['colaborador']

    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=True, blank=True)

# Create your models here.
