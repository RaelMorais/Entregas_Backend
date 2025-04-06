from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Usuario
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .serializer import UsuarioSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Usuario



@api_view(['POST'])
def create_user(request):
    # Obtendo os dados do request
    username = request.data.get('username')
    password = request.data.get('password')
    data_nascimento = request.data.get('data_nascimento')
    idade = request.data.get('idade')
    biografia = request.data.get('biografia')
    telefone = request.data.get('telefone')
    escolaridade = request.data.get('escolaridade')
    
    # Endereço
    rua = request.data.get('rua')
    numero = request.data.get('numero')
    cidade = request.data.get('cidade')
    estado = request.data.get('estado')
    cep = request.data.get('cep')
    pais = request.data.get('pais')
    
    # Informações do animal
    nome_animal = request.data.get('nome_animal')
    especie_animal = request.data.get('especie_animal')
    qtd_animais = request.data.get('qtd_animais')

    # Verificação de campos obrigatórios
    if not username or not password or not data_nascimento or not idade or not rua or not cidade or not estado or not cep or not pais:
        return Response({'Erro': 'Campos obrigatórios incompletos'}, status=status.HTTP_400_BAD_REQUEST)

    # Verificando se o username já existe
    if Usuario.objects.filter(username=username).exists():
        return Response({'Erro': f'Username {username} já existe'}, status=status.HTTP_400_BAD_REQUEST)
    
    # Criando o usuário
    usuario = Usuario.objects.create_user(
        username=username,
        password=password,
        data_nascimento=data_nascimento,
        idade=idade,
        biografia=biografia,
        telefone=telefone,
        escolaridade=escolaridade,
        rua=rua,
        numero=numero,
        cidade=cidade,
        estado=estado,
        cep=cep,
        pais=pais,
        nome_animal=nome_animal,
        especie_animal=especie_animal,
        qtd_animais=qtd_animais
    )

    # Retornando a resposta de sucesso
    return Response({'Mensagem': f'Usuário {username} criado com sucesso'}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    usuario = authenticate(username=username, password=password)

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
def root(request):
    usuario = request.user 
    serializer = UsuarioSerializer(usuario)
    return Response(serializer.data)


class PutDeleteClass(RetrieveUpdateDestroyAPIView): #generic view para GET, PUT, DELETE 
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        usuario = self.get_object() 
        usuario.delete()
        return Response({"message":"Usuario dleetado com sucesso"}, status=status.HTTP_204_NO_CONTENT)
# {
# "username":"joao123",
# "password":"senha123"
# }