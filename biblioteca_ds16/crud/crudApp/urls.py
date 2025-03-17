from django.urls import path
from . import views

urlpatterns =[
    path('', views.livro_list, name='livro_list'), 
    path('livros/novo/', views.livro_create, name='livro_create'),
    path('livros/editar/<int:pk>/', views.livro_update, name='livro_update'),
    path('livros/deletar/<int:pk>/', views.livro_delete, name='livro_delete'),
    path('autores/', views.autor_list, name='autor_list'),
    path('autores/novo/', views.create_autor, name='create_autor'),
    path('autores/editar/<int:pk>/', views.update_autor, name='update_autor'),
    path('autores/excluir/<int:pk>/', views.delete_autor, name='delete_autor'),
    path('filtro', views.livros_filters, name='livros_filter'),
]