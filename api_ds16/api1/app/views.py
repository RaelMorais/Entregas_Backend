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
# Create your views here.

@api_view(['POST'])
def add_cars(request):
        cars_data = [
            {"name_car": "Corolla", "name_factory": "Toyota", "horsepower": 139, "category": "Sedan", "qty_ports": 4, "qty_roads": 4, "color": "Silver", "year": 2020, "fuel": "gs"},
            {"name_car": "Civic", "name_factory": "Honda", "horsepower": 158, "category": "Sedan", "qty_ports": 4, "qty_roads": 4, "color": "Black", "year": 2021, "fuel": "gs"},
            {"name_car": "Focus", "name_factory": "Ford", "horsepower": 160, "category": "Hatchback", "qty_ports": 5, "qty_roads": 4, "color": "Blue", "year": 2019, "fuel": "gs"},
            {"name_car": "Cruze", "name_factory": "Chevrolet", "horsepower": 153, "category": "Sedan", "qty_ports": 4, "qty_roads": 4, "color": "Red", "year": 2018, "fuel": "gs"},
            {"name_car": "320i", "name_factory": "BMW", "horsepower": 255, "category": "Sedan", "qty_ports": 4, "qty_roads": 4, "color": "White", "year": 2020, "fuel": "gs"},
            {"name_car": "A4", "name_factory": "Audi", "horsepower": 190, "category": "Sedan", "qty_ports": 4, "qty_roads": 4, "color": "Gray", "year": 2021, "fuel": "gs"},
            {"name_car": "Golf", "name_factory": "Volkswagen", "horsepower": 147, "category": "Hatchback", "qty_ports": 5, "qty_roads": 4, "color": "Green", "year": 2019, "fuel": "gs"},
            {"name_car": "C-180", "name_factory": "Mercedes-Benz", "horsepower": 255, "category": "Sedan", "qty_ports": 4, "qty_roads": 4, "color": "Silver", "year": 2020, "fuel": "gs"},
            {"name_car": "Altima", "name_factory": "Nissan", "horsepower": 182, "category": "Sedan", "qty_ports": 4, "qty_roads": 4, "color": "Black", "year": 2021, "fuel": "gs"},
            {"name_car": "Elantra", "name_factory": "Hyundai", "horsepower": 147, "category": "Sedan", "qty_ports": 4, "qty_roads": 4, "color": "Blue", "year": 2020, "fuel": "gs"},
            {"name_car": "Accord", "name_factory": "Honda", "horsepower": 192, "category": "Sedan", "qty_ports": 4, "qty_roads": 4, "color": "Silver", "year": 2021, "fuel": "gs"},
            {"name_car": "Model 3", "name_factory": "Tesla", "horsepower": 283, "category": "Sedan", "qty_ports": 4, "qty_roads": 4, "color": "White", "year": 2021, "fuel": "ev"},
            {"name_car": "Bolt EV", "name_factory": "Chevrolet", "horsepower": 200, "category": "Hatchback", "qty_ports": 5, "qty_roads": 4, "color": "Blue", "year": 2022, "fuel": "ev"},
            {"name_car": "Mustang", "name_factory": "Ford", "horsepower": 450, "category": "Coupe", "qty_ports": 2, "qty_roads": 2, "color": "Yellow", "year": 2021, "fuel": "gs"},
            {"name_car": "911", "name_factory": "Porsche", "horsepower": 379, "category": "Coupe", "qty_ports": 2, "qty_roads": 2, "color": "Red", "year": 2021, "fuel": "gs"},
            {"name_car": "X5", "name_factory": "BMW", "horsepower": 335, "category": "SUV", "qty_ports": 4, "qty_roads": 4, "color": "Black", "year": 2022, "fuel": "gs"},
            {"name_car": "Grand Cherokee", "name_factory": "Jeep", "horsepower": 290, "category": "SUV", "qty_ports": 4, "qty_roads": 4, "color": "Silver", "year": 2020, "fuel": "gs"},
            {"name_car": "Q7", "name_factory": "Audi", "horsepower": 333, "category": "SUV", "qty_ports": 4, "qty_roads": 4, "color": "Green", "year": 2021, "fuel": "gs"},
            {"name_car": "RAV4", "name_factory": "Toyota", "horsepower": 203, "category": "SUV", "qty_ports": 4, "qty_roads": 4, "color": "White", "year": 2021, "fuel": "gs"},
            {"name_car": "Model X", "name_factory": "Tesla", "horsepower": 670, "category": "SUV", "qty_ports": 4, "qty_roads": 4, "color": "Blue", "year": 2021, "fuel": "ev"},
            {"name_car": "Leaf", "name_factory": "Nissan", "horsepower": 147, "category": "Hatchback", "qty_ports": 5, "qty_roads": 4, "color": "Silver", "year": 2020, "fuel": "ev"},
            {"name_car": "Spark", "name_factory": "Chevrolet", "horsepower": 98, "category": "Hatchback", "qty_ports": 5, "qty_roads": 4, "color": "Black", "year": 2021, "fuel": "gs"},
            {"name_car": "MX-3", "name_factory": "Mazda", "horsepower": 155, "category": "Sedan", "qty_ports": 4, "qty_roads": 4, "color": "Yellow", "year": 2020, "fuel": "gs"},
            {"name_car": "Optima", "name_factory": "Kia", "horsepower": 178, "category": "Sedan", "qty_ports": 4, "qty_roads": 4, "color": "Red", "year": 2020, "fuel": "gs"}
        ]

        for car_data in cars_data:
                Car.objects.create(**car_data)

        return Response({"message": "25 carros adicionados com sucesso!"})