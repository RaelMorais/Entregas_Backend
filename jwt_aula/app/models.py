from django.db import models
from django.contrib.auth.models import AbstractUser

class UsuarioDS16(AbstractUser):
    data_nascimento = models.DateField()
    apelido = models.CharField(max_length=255, null=True, blank=True)
    edv = models.PositiveIntegerField(max_length=255, null=True, blank=True)
    padrinho = models.CharField(max_length=255, null=True, blank=True)
    REQUIRED_FIELDS = ['data_nascimento']
    """
    Modelo de usuário personalizado que herda de AbstractUser do Django e adiciona 
    campos específicos para o sistema, como data de nascimento, apelido, EDV (número de identificação) 
    e padrinho. Este modelo é utilizado para registrar usuários com atributos extras.

    Atributos:
        username (str): O nome de usuário único para autenticação, herdado de AbstractUser.
        first_name (str): O primeiro nome do usuário, herdado de AbstractUser.
        last_name (str): O sobrenome do usuário, herdado de AbstractUser.
        email (str): O email do usuário, herdado de AbstractUser.
        data_nascimento (date): Data de nascimento do usuário, não pode ser nula.
        apelido (str): Apelido do usuário, pode ser nulo ou em branco.
        edv (int): Número de identificação único (EDV) do usuário, pode ser nulo ou em branco.
        padrinho (str): Nome do padrinho do usuário, pode ser nulo ou em branco.

    Métodos:
        __str__(): Retorna o nome de usuário como representação de string do objeto.
    
    Notas:
        - A classe herda de `AbstractUser`, que fornece os campos padrão do Django para usuários, como 
          `username`, `password`, `email`, etc.
        - O campo `edv` é do tipo `PositiveIntegerField`, o que significa que o valor deve ser um número inteiro
          positivo.
        - O campo `REQUIRED_FIELDS` especifica que `data_nascimento` é um campo obrigatório durante a criação 
          de um usuário via Django Admin ou outras interfaces de gerenciamento.
    """

    def __str__(self):
        return self.username 






# Create your models here.
