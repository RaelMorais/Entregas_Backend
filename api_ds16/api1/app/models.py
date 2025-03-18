from django.db import models

#Criando o modelo do banco de dados. 

class Car(models.Model):
    name_car = models.CharField(max_length=255) #Nome do carro. 
    name_factory = models.CharField(max_length=255) #Nome da fabricante.  
    horsepower = models.FloatField() #Potencia do carro. 
    category = models.CharField(max_length=255) #Categoria que o carro pertence; 
    qty_ports = models.PositiveIntegerField() #Quantidade de Portas no carro. 
    qty_roads = models.PositiveIntegerField() #Qauntidade de rodas
    color = models.CharField(max_length=255) #Cor do carro. 
    year = models.PositiveIntegerField() #Ano que o carro pertence. 
    '''
    Criando uma lista com 7 tipos de combustiveis, e definindo ela como escolhas do "fuel"
    Podendo escolher 7 opções, entretanto, para futuras melhorias, o tamanho máximo de escolha é 9. 

    '''
    choice_fuel = (
        ('gs', 'Gasoline'),
        ('gnv', 'Compressed Natural Gas'),
        ('al', 'Ethanol'),
        ('ev', 'Electric'),
        ('ds', 'Diesel'),
        ('bd', 'Biodiesel'),
        ('bs', 'Biofuel'), 
    )
    fuel = models.CharField(max_length=9, choices=choice_fuel)

    def __str__(self): #Retornando um valor ao salvar o banco. 
        return "Deu certo!"
# Create your models here.
