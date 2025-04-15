from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import *
from .serializers import * 
from rest_framework.pagination import PageNumberPagination
from rest_framework import serializers
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class CarroPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10

@swagger_auto_schema(
    operation_description='Lista todos os pilotos',
    responses={
        200: PilotoSerializer(many=True),
        400: 'Error',
    },
    manual_parameters=[
        openapi.Parameter(
            'nome', 
            openapi.IN_QUERY,
            description = 'Filtrar pelo nome do piloto', 
            type=openapi.TYPE_STRING
        )
    ]
        
)
def get(self, request, *args, **kwargs):
    return super().get(request, *args, **kwargs)

@swagger_auto_schema(
    operation_description='Cria um novo piloto',
    request_body=PilotoSerializer,
    responses={
        201: PilotoSerializer,
        400: 'Erro'
    }
)
def post(self, request, *args, **kwargs):
    return super().post(request, *args, **kwargs)

class PilotoPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10

class GetPostPiloto(ListCreateAPIView):
    queryset = Piloto.objects.all()
    serializer_class = PilotoSerializer
    pagination_class = PilotoPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.query_params.get('nome')
        if nome:
           queryset = queryset.filter(nome__icontains=nome)
        return queryset
    
    def perform_create(self, serializer):
        # Garantir que 'classificacao' seja comparado com um valor numérico
        if serializer.validated_data['time'] != 'Red Bull' and serializer.validated_data['classificacao'] <= 5:
            raise serializers.ValidationError('Somente a red bull pode ganhar')
        serializer.save()

class PilotoUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Piloto.objects.all()
    serializer_class = PilotoSerializer
    lookup_field = 'pk'

    @swagger_auto_schema(
        operation_description='Pega o piloto do id fornecido',
        responses={
            200: PilotoSerializer,
            404: 'Not Found', 
            400: 'Error'
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class GetPostCarro(ListCreateAPIView):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer
    pagination_class = CarroPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.query_params.get('nome')
        if nome:
           queryset = queryset.filter(nome__icontains=nome)
        return querys

    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.query_params.get('nome')
        if nome:
           queryset = queryset.filter(nome__icontains=nome)
        return queryset
    
    def perform_create(self, serializer):
        # Corrigido para utilizar validated_data corretamente
        if serializer.validated_data['nome'] != 'Red Bull Honda' and serializer.validated_data['marca'] == "Red Bull":
            raise serializers.ValidationError('Somente a red bull pode ganhar')
        serializer.save()

class CarroUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer
    lookup_field = 'pk'

@swagger_auto_schema(
    operation_description='Lista todos os pilotos',
    responses={
        200: CarroSerializer(many=True),
        400: 'Error',
    },
    manual_parameters=[
        openapi.Parameter(
            'nome', 
            openapi.IN_QUERY,
            description = 'Filtrar pelo nome do piloto', 
            type=openapi.TYPE_STRING
        )
    ]
        
)
def get(self, request, *args, **kwargs):
    return super().get(request, *args, **kwargs)

@swagger_auto_schema(
    operation_description='Cria um novo piloto',
    request_body=CarroSerializer,
    responses={
        201: CarroSerializer,
        400: 'Erro'
    }
)
def post(self, request, *args, **kwargs):
    return super().post(request, *args, **kwargs)

# Create your views here.



# Fazer swagger carro do get, post, delete, put de todos piloto e carro