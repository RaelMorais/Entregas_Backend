from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import *
from .serializers import * 
from rest_framework.pagination import PageNumberPagination
from rest_framework import serializers
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


# Paginação piloto e carro 

class CarroPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10


class PilotoPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10


# Piloto views 
class GetPostPiloto(ListCreateAPIView):
    queryset = Piloto.objects.all()
    serializer_class = PilotoSerializer
    pagination_class = PilotoPagination

    # Descrição do GET no Swagger
    @swagger_auto_schema(
        operation_description='Listar todos os pilotos', 
        responses={
                   200: PilotoSerializer(many=True),
            400: 'Error', 

        },
        manual_parameters=[
            openapi.Parameter(
                'nome', 
                openapi.IN_QUERY,
                description='Filtrar pelo nome do piloto', 
                type=openapi.TYPE_STRING
            )
        ]   
    )
    # Função para buscar piloto por nome 
    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.query_params.get('nome')
        if nome:
           queryset = queryset.filter(nome__icontains=nome)
        return queryset
        
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


     # Descrição do Post no Swagger 
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

    def perform_create(self, serializer):
        #Garante que 'classificacao' seja comparado com um valor numérico
        if serializer.validated_data['time'] != 'Red Bull' and serializer.validated_data['classificacao'] <= 5:
            raise serializers.ValidationError('Somente a red bull pode ganhar')
        serializer.save()


class PilotoUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Piloto.objects.all()
    serializer_class = PilotoSerializer
    lookup_field = 'pk'

    # Para adicionar descrição no método GET do swagger. 
    @swagger_auto_schema(
        operation_description='Retorna os detalhes do piloto pelo ID',
        responses={
            200: PilotoSerializer,  # Retorna as informações do piloto
            404: 'Não encontrado',  # Caso o piloto não seja encontrado
            400: 'Erro na requisição',  # Erro genérico
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    # Para adicionar descrição no método PUT do swagger para pilotos. 
    @swagger_auto_schema(
        operation_description='Atualiza informações de um piloto por ID.',
        request_body=PilotoSerializer,
        responses={
            201: PilotoSerializer,
            400: 'Erro',
            404: 'Not Found', 
        }
    )

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    # Para deletar piloto do swagger. 
    @swagger_auto_schema(
        operation_description='Deleta o piloto pelo ID',
        responses={
            204: 'Deletado com sucesso!',  # Resposta de sucesso, sem conteúdo
            404: 'Não encontrado',  # Caso o piloto não seja encontrado
        }
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


# Carrro views
class GetPostCarro(ListCreateAPIView):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer
    pagination_class = CarroPagination

    # Descrição do GET no Swagger
    @swagger_auto_schema(
        operation_description='Listar todos os carros', 
        responses={
            200: CarroSerializer(many=True),
            400: 'Error', 

        },
        manual_parameters=[
            openapi.Parameter(
                'nome', 
                openapi.IN_QUERY,
                description='Filtrar pelo nome do carro', 
                type=openapi.TYPE_STRING
            )
        ]   
    )

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.query_params.get('nome')
        if nome:
           queryset = queryset.filter(nome__icontains=nome)
        return queryset
    
    # Descrição para criar o carro
    @swagger_auto_schema(
        operation_description='Cria um novo carro',
        request_body=CarroSerializer,
        responses={
            201: CarroSerializer,
            400: 'Erro'
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


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
        operation_description='Deleta o carro pelo ID',
        responses={
            204: 'Deletado com sucesso!',  # Resposta de sucesso, sem conteúdo
            404: 'Não encontrado',  # Caso o carro não seja encontrado
        }
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


    # Para adicionar descrição no método GET do swagger. 
    @swagger_auto_schema(
        operation_description= "ssssssssssssssss",
        responses={
            200: CarroSerializer,
            404: 'Not found', 
            400: 'Request Error', 
        }

    )

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    # Para adicionar descrição no método PUT do swagger para pilotos. 
    @swagger_auto_schema(
        operation_description='Atualiza informações de um carro por ID.',
        request_body=CarroSerializer,
        responses={
            201: CarroSerializer,
            400: 'Erro',
            404: 'Not Found', 
        }
    )

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    # Para deletar piloto do swagger. 




# Create your views here.



# Fazer swagger carro do get, post, delete, put de todos piloto e carro