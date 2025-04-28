from django.shortcuts import render
from .permissions import *
from rest_framework.generics import ListCreateAPIView
from .serializers import *

class teste(ListCreateAPIView):
    serializer_class = UsuarioSerializer
    permission_classes = [IsGestor]
# Create your views here.
