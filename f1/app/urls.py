from django.urls import path
from .views import * 
from . import views

urlpatterns = [
   path("piloto/", views.GetPostPiloto.as_view()),
   path('carro/', views.GetPostCarro.as_view()),
]
