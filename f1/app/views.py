from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import *
from .serializers import * 
from rest_framework.pagination import PageNumberPagination


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
    
class GetPostCarro(ListCreateAPIView):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.query_params.get('nome')
        if nome:
           queryset = queryset.filter(nome__icontains=nome)
        return queryset
# Create your views here.

