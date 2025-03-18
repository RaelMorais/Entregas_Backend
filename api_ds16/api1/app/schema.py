import graphene
from graphene_django.types import DjangoObjectType
from .models import Car #Modelos aqui 

#Definindo o tipo Car para GraphQL, definindo dados 
class CarType(DjangoObjectType):
    class Meta:
        model = Car # Define que o modelo a ser usado é = db Car
        fields = ("id", "name_car", "name_factory", "horsepower", "category", "qty_ports", "qty_roads", "color", "year", "fuel")

#Definindo a consulta (Query)
class Query(graphene.ObjectType):
    car = graphene.Field(CarType, id=graphene.Int()) 
    cars = graphene.List(CarType) 

    def resolve_car(self, info, id):
        return Car.objects.get(id=id) 

  
    def resolve_cars(self, info):
        return Car.objects.all() 
#Definindo o schema GraphQL
schema = graphene.Schema(query=Query)
