from django.db import models

class Autor(models.Model):
    nome_autor = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return self.nome_autor
class Genero(models.Model):

    genero = models.CharField(max_length=255)
    def __str__(self):
         return self.genero

class Livros(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.ForeignKey(Autor, related_name='livros', on_delete=models.CASCADE)
    genero= models.ForeignKey(Genero, related_name='Livros', on_delete=models.CASCADE)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    resumo = models.TextField()
    ISBN = models.IntegerField(max_length=13)

    def __str__(self):
        return self.titulo

# Create your models here.
