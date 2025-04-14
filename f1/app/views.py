from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import *
from .serializers import * 
from rest_framework.pagination import PageNumberPagination
from rest_framework import serializers


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
        
class GetPostCarro(ListCreateAPIView):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer

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



# Create your views here.

