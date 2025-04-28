from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import *
from .serializers import * 
from rest_framework.pagination import PageNumberPagination
from rest_framework import serializers
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


# Paginação para Piloto e Carro
class CarroPagination(PageNumberPagination):
    page_size = 5  # Define o número de itens por página
    page_size_query_param = 'page_size'  # Permite que o cliente altere o número de itens por página
    max_page_size = 10  # Define o número máximo de itens por página

class PilotoPagination(PageNumberPagination):
    page_size = 5  # Define o número de itens por página
    page_size_query_param = 'page_size'  # Permite que o cliente altere o número de itens por página
    max_page_size = 10  # Define o número máximo de itens por página


# View para listar e criar Pilotos
class GetPostPiloto(ListCreateAPIView):
    queryset = Piloto.objects.all()  # Obtém todos os pilotos
    serializer_class = PilotoSerializer  # Define o serializer para a resposta
    pagination_class = PilotoPagination  # Define a classe de paginação

    # Descrição do GET no Swagger
    @swagger_auto_schema(
        operation_description='Listar todos os pilotos', 
        responses={
            200: PilotoSerializer(many=True),  # Retorna a lista de pilotos
            400: 'Error',  # Resposta em caso de erro
        },
        manual_parameters=[
            openapi.Parameter(
                'nome', 
                openapi.IN_QUERY,  # Parâmetro de consulta para filtragem
                description='Filtrar pelo nome do piloto', 
                type=openapi.TYPE_STRING
            )
        ]   
    )
    def get_queryset(self):
        # Filtra os pilotos com base no nome (se fornecido)
        queryset = super().get_queryset()
        nome = self.request.query_params.get('nome')
        if nome:
            queryset = queryset.filter(nome__icontains=nome)  # Filtra os pilotos pelo nome
        return queryset
        
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    # Descrição do POST no Swagger 
    @swagger_auto_schema(
        operation_description='Cria um novo piloto',
        request_body=PilotoSerializer,  # Corpo da requisição para criar o piloto
        responses={
            201: PilotoSerializer,  # Retorna o piloto criado
            400: 'Erro'  # Resposta em caso de erro
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def perform_create(self, serializer):
        # Garante que apenas pilotos com classificação <= 5 possam ser criados, exceto Red Bull
        if serializer.validated_data['time'] != 'Red Bull' and serializer.validated_data['classificacao'] <= 5:
            raise serializers.ValidationError('Somente a Red Bull pode ganhar')
        serializer.save()


# View para atualizar, excluir e obter um único Piloto
class PilotoUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Piloto.objects.all()  # Obtém todos os pilotos
    serializer_class = PilotoSerializer  # Define o serializer
    lookup_field = 'pk'  # O campo de busca é o 'pk' (id do piloto)

    # Descrição do GET no Swagger (detalhes do piloto por ID)
    @swagger_auto_schema(
        operation_description='Retorna os detalhes do piloto pelo ID',
        responses={
            200: PilotoSerializer,  # Retorna os dados do piloto
            404: 'Não encontrado',  # Caso o piloto não seja encontrado
            400: 'Erro na requisição',  # Erro genérico
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    # Descrição do PUT no Swagger (atualiza o piloto)
    @swagger_auto_schema(
        operation_description='Atualiza informações de um piloto por ID.',
        request_body=PilotoSerializer,  # Corpo da requisição com dados atualizados
        responses={
            201: PilotoSerializer,  # Retorna o piloto atualizado
            400: 'Erro',  # Caso haja erro na requisição
            404: 'Não encontrado',  # Caso o piloto não seja encontrado
        }
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    # Descrição do DELETE no Swagger (deleta o piloto)
    @swagger_auto_schema(
        operation_description='Deleta o piloto pelo ID',
        responses={
            204: 'Deletado com sucesso!',  # Resposta de sucesso, sem conteúdo
            404: 'Não encontrado',  # Caso o piloto não seja encontrado
        }
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


# View para listar e criar Carros
class GetPostCarro(ListCreateAPIView):
    queryset = Carro.objects.all()  # Obtém todos os carros
    serializer_class = CarroSerializer  # Define o serializer para a resposta
    pagination_class = CarroPagination  # Define a classe de paginação

    # Descrição do GET no Swagger
    @swagger_auto_schema(
        operation_description='Listar todos os carros', 
        responses={
            200: CarroSerializer(many=True),  # Retorna a lista de carros
            400: 'Erro',  # Resposta em caso de erro
        },
        manual_parameters=[
            openapi.Parameter(
                'nome', 
                openapi.IN_QUERY,  # Parâmetro de consulta para filtragem
                description='Filtrar pelo nome do carro', 
                type=openapi.TYPE_STRING
            )
        ]   
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        # Filtra os carros com base no nome (se fornecido)
        queryset = super().get_queryset()
        nome = self.request.query_params.get('nome')
        if nome:
            queryset = queryset.filter(nome__icontains=nome)  # Filtra os carros pelo nome
        return queryset
    
    # Descrição para criar um carro
    @swagger_auto_schema(
        operation_description='Cria um novo carro',
        request_body=CarroSerializer,  # Corpo da requisição para criar o carro
        responses={
            201: CarroSerializer,  # Retorna o carro criado
            400: 'Erro'  # Resposta em caso de erro
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def perform_create(self, serializer):
        # Garante que apenas carros com a marca "Red Bull" possam ser criados
        if serializer.validated_data['nome'] != 'Red Bull Honda' and serializer.validated_data['marca'] == "Red Bull":
            raise serializers.ValidationError('Somente a Red Bull pode ganhar')
        serializer.save()

# View para atualizar, excluir e obter um único Carro
class CarroUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Carro.objects.all()  # Obtém todos os carros
    serializer_class = CarroSerializer  # Define o serializer
    lookup_field = 'pk'  # O campo de busca é o 'pk' (id do carro)

    # Descrição do DELETE no Swagger (deleta o carro)
    @swagger_auto_schema(
        operation_description='Deleta o carro pelo ID',
        responses={
            204: 'Deletado com sucesso!',  # Resposta de sucesso, sem conteúdo
            404: 'Não encontrado',  # Caso o carro não seja encontrado
        }
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    # Descrição do GET no Swagger (detalhes do carro por ID)
    @swagger_auto_schema(
        operation_description='Retorna os detalhes do carro pelo ID',
        responses={
            200: CarroSerializer,  # Retorna os dados do carro
            404: 'Não encontrado',  # Caso o carro não seja encontrado
            400: 'Erro na requisição',  # Erro genérico
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    # Descrição do PUT no Swagger (atualiza o carro)
    @swagger_auto_schema(
        operation_description='Atualiza informações de um carro por ID.',
        request_body=CarroSerializer,  # Corpo da requisição com dados atualizados
        responses={
            201: CarroSerializer,  # Retorna o carro atualizado
            400: 'Erro',  # Caso haja erro na requisição
            404: 'Não encontrado',  # Caso o carro não seja encontrado
        }
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

