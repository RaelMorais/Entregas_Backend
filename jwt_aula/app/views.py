from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework import status
from .models import UsuarioDS16

@api_view(['POST'])
def criar_usuario(request):
    username = request.data.get('username')
    senha = request.data.get('senha')
    edv = request.data.get('edv')
    data_nascimento = request.data.get('data_nascimento')
    padrinho = request.data.get('padrinho')
    apelido = request.data.get('apelido')

    if not username or not senha or not edv or not data_nascimento :
        return Response({'Erro':'Campos obrigatorios incompletos'}, status=status.HTTP_400_BAD_REQUEST)
    
    if UsuarioDS16.objects.filter(username=username).exists():
        return Response({'Erro':f'Username {username} já existe'}, status=status.HTTP_400_BAD_REQUEST)
    
    if UsuarioDS16.objects.filter(edv=edv).exists():
        return Response({'Erro':f'EDV {edv} já existe'}, status=status.HTTP_400_BAD_REQUEST)
    
    usuario = UsuarioDS16.objects.create_user(
        username=username,
        password=senha,
        data_nascimento=data_nascimento,
        padrinho=padrinho,
        apelido=apelido,
        email='Lini@mail.com'
    )

    return Response({'Mensagem': f'Usuario {username} criado com sucesso'}, status=status.HTTP_201_CREATED)
# Create your views here.
