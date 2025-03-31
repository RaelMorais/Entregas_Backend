from django.db import models
from django.contrib.auth.models import AbstractUser

class UsuarioDS16(AbstractUser):
    data_nascimento = models.DateField()
    apelido = models.CharField(max_length=255, null=True, blank=True)
    edv = models.PositiveIntegerField()
    padrinho = models.CharField(max_length=255, null=True, blank=True)
    REQUIRED_FIELDS = ['data_nascimento', 'edv']

    def __str__(self):
        return self.username 






# Create your models here.
