from django.urls import path
from . import views  

urlpatterns = [
    path('criar/', views.criar_usuario, name='criar_usuario'),  # Views para Criar usuario usa a def criar_usuario em Views. 
    path('logar/', view=views.logar_user, name='logar_usuario'), # View para logar usuario, usando a def logar_user em Views.
    path('read/', view=views.read_view, name='Teste'),
]
