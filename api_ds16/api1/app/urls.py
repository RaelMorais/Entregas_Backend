from django.urls import path 
from . import views

urlpatterns = [
    path("api/", views.read_cars),
    path('cars/search/<int:pk>', views.show_car),
    path('add/', views.add_cars, name='add_cars'),
]