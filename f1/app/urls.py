from django.urls import path
from .views import *  # Importa todas as views definidas em views.py
from . import views  # Também importa views de forma explícita
from drf_yasg import openapi  # Importa o módulo para a documentação Swagger
from drf_yasg.views import get_schema_view  # Função para gerar a documentação Swagger
from rest_framework import permissions  # Para configurar permissões de acesso

# Configuração da visualização do esquema de documentação com Swagger e ReDoc
schema_view = get_schema_view(
    openapi.Info(
        title="API da Fórmula 1",  # Título da documentação da API
        default_version='v1',  # Versão padrão da API
        description="Documentação da API para dados da Fórmula 1",  # Descrição breve da API
    ),
    public=True,  # Define a documentação como pública
    permission_classes=(permissions.AllowAny,),  # Permite o acesso a qualquer usuário sem restrições
)

# Definição das URLs da API
urlpatterns = [
    # URL para listar e criar pilotos
    path("piloto/", views.GetPostPiloto.as_view()),

    # URL para listar e criar carros
    path('carro/', views.GetPostCarro.as_view()),

    # URL para obter, atualizar ou excluir um piloto específico (usando o ID 'pk')
    path('piloto/<int:pk>', views.PilotoUpdateDelete.as_view()),

    # URL para obter, atualizar ou excluir um carro específico (usando o ID 'pk')
    path('carro/<int:pk>', views.CarroUpdateDelete.as_view()),

    # URL para a interface de documentação do ReDoc (formato mais amigável)
    path('redoc/', view=schema_view.with_ui('redoc', cache_timeout=0)),

    # URL para a interface de documentação do Swagger (formato interativo)
    path('doc/', view=schema_view.with_ui('swagger', cache_timeout=0)),
]
