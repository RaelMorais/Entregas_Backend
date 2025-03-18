from django.urls import path 
from . import views
from graphene_django.views import GraphQLView
from app.schema import schema  

urlpatterns = [
    path("api/", views.read_cars),
    path('cars/search/<int:pk>', views.show_car),
    path('add/', views.add_cars, name='add_cars'),
    path('create/', views.create_car),
    path('cars/update/<int:pk>', views.update_car),
    path('cars/delete/<int:pk>', views.delete_car),
    path('graphql/', GraphQLView.as_view(graphiql=True, schema=schema)),
]   