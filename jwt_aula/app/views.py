from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response 
from rest_framework import status
from .models import UsuarioDS16
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
@api_view(['POST'])
def criar_usuario(request):
    """
    Cria um novo usuário.

    Recebe os dados necessários para criar um usuário (username, senha, edv, data_nascimento, etc.).
    Verifica se os campos obrigatórios estão presentes, se o username e o edv já não existem.
    Se tudo estiver correto, cria o usuário e retorna uma resposta de sucesso.
    
    Parâmetros esperados:
        - username (str): Nome de usuário.
        - senha (str): Senha do usuário.
        - edv (str): Número de identificação único (EDV).
        - data_nascimento (date): Data de nascimento.
        - padrinho (str, opcional): Nome do padrinho.
        - apelido (str, opcional): Apelido do usuário.
    
    Respostas possíveis:
        - 201 Created: Usuário criado com sucesso.
        - 400 Bad Request: Campos obrigatórios incompletos ou dados duplicados (username/EDV).

    """
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



@api_view(['POST'])
def logar_user(request):
    """
    Realiza o login do usuário e retorna tokens JWT.

    Verifica as credenciais (username e senha) do usuário. Se válidas, gera e retorna os tokens 
    de acesso e refresh. Caso contrário, retorna um erro de autenticação.
    
    Parâmetros esperados:
        - username (str): Nome de usuário.
        - senha (str): Senha do usuário.

    Respostas possíveis:
        - 200 OK: Retorna os tokens (acesso e refresh).
        - 401 Unauthorized: Erro de autenticação (usuario ou senha incorretos).
    """
    username = request.data.get('username')
    senha = request.data.get('senha')

    usuario = authenticate(username=username, password=senha)

    if usuario:
        refresh = RefreshToken.for_user(usuario)
        return Response({
            'acesso':str(refresh.access_token),
            'refresh': str(refresh),

        }, status=status.HTTP_200_OK)
    else:
        return Response({'Erro': 'Usuario ou/e senha incorreto'}, status=status.HTTP_401_UNAUTHORIZED)
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def read_view(request):
    return Response({'message':'Ola mundo!'}, status=status.HTTP_200_OK)
# Create your views here.
