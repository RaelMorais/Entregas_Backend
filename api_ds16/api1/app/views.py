from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Car
from .serializers import CarSerializer
from rest_framework import status

@api_view(['GET'])
def read_cars(request):
    cars = Car.objects.all()
    serializer = CarSerializer(cars, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def show_car(request, pk):
    try:
        cars = Car.objects.get(pk=pk)
    except Car.DoesNotExist:
        return Response({'Error':'Car does not exist'}, status=status.HTTP_404_NOT_FOUND)

    serializer = CarSerializer(cars)
    return Response(serializer.data)


@api_view(['POST'])
def create_car(request):
     if request.method == 'POST':
          serializer = CarSerializer(data=request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data, status=status.HTTP_201_CREATED)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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


@api_view(['DELETE'])
def delete_car(request, pk):
    try:
          car = Car.objects.get(pk=pk)
    except Car.DoesNotExist:
        return Response({'erro':'Carro inexistente'}, status=status.HTTP_404_NOT_FOUND)
    car.delete()
    return Response({'message': 'Carro deletado com sucesso'}, status=status.HTTP_200_OK)

@api_view(['POST'])
def add_cars(request):
        cars_data = [

        ]

        for car_data in cars_data:
                Car.objects.create(**car_data)

        return Response({"message": "25 carros adicionados com sucesso!"})