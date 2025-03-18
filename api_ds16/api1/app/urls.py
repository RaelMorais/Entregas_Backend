from django.urls import path 
from . import views
from graphene_django.views import GraphQLView
from app.schema import schema  

'''
Criando Urls para centralizar todos os Endpoints da API 

api/ lista todos os itens.
add/ cria um post para uma lista de carros.
create/ para inserir um novo dado no banco.
cars/update/<> atualizar um carro pelo Id
cars/dele/<> deleter um carro pelo ID
graphql/ para acessar interface do GraphQL



'''
urlpatterns = [
    path("api/", views.read_cars),
    path('cars/search/<int:pk>', views.show_car),
    path('add/', views.add_cars, name='add_cars'),
    path('create/', views.create_car),
    path('cars/update/<int:pk>', views.update_car),
    path('cars/delete/<int:pk>', views.delete_car),
    path('graphql/', GraphQLView.as_view(graphiql=True, schema=schema)),
]   