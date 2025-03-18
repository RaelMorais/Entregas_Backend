from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Car
from .serializers import CarSerializer
from rest_framework import status


'''
View criada em Funções Baseadas em Funções - FBV

Usa o método Get para buscar todos os objetos no banco de dados, depois torna cada item um objeto de um Json 
retornando todos os dados serializados. 

'''
@api_view(['GET'])
def read_cars(request):
    cars = Car.objects.all()
    serializer = CarSerializer(cars, many=True)
    return Response(serializer.data)




'''
Método GET para buscar um dado pelo ID especifico, onde trás todos os objetos do Id especifico, 
depois serializa e transforma em objetos de um JSON, 
caso o carro não seja encontrando, retorna uma mensagem de erro e o Status Code do erro. 

'''

@api_view(['GET'])
def show_car(request, pk):
    try:
        cars = Car.objects.get(pk=pk)
    except Car.DoesNotExist:
        return Response({'Error':'Car does not exist'}, status=status.HTTP_404_NOT_FOUND)

    serializer = CarSerializer(cars)
    return Response(serializer.data)

'''
View criada para inserir dados no banco de dados, onde caso os dados 
consigam ser carregados do Json(Serializados) 
e retornem para o banco de forma válida, ira salvar e caso haja algum erro, retorna 400_BAD_REQUEST


'''

@api_view(['POST'])
def create_car(request):
     if request.method == 'POST':
          serializer = CarSerializer(data=request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data, status=status.HTTP_201_CREATED)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



'''
view criada para atualizar dados dentro do banco, onde verifica se os dados são válidos e salva no banco. 

'''
@api_view(['PUT'])
def update_car(request, pk):
    try:
          car = Car.objects.get(pk=pk)
    except Car.DoesNotExist:
        return Response({'erro':'Carro inexistente'}, status=status.HTTP_404_NOT_FOUND)
     
    serializer = CarSerializer(car,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

'''
view criada para buscar um dado especifico pelo id, e caso seja encontrada, excluir do banco, 
caso não encontre irá retornar um erro 404 de não encontrado. 

'''

@api_view(['DELETE'])
def delete_car(request, pk):
    try:
          car = Car.objects.get(pk=pk)
    except Car.DoesNotExist:
        return Response({'erro':'Carro inexistente'}, status=status.HTTP_404_NOT_FOUND)
    car.delete()
    return Response({'message': 'Carro deletado com sucesso'}, status=status.HTTP_200_OK)

'''
view criada para salvar uma lista de itens dentro do banco de dados. 

'''
@api_view(['POST'])
def add_cars(request):
        cars_data = [

        ]

        for car_data in cars_data:
                Car.objects.create(**car_data)

        return Response({"message": "25 carros adicionados com sucesso!"})