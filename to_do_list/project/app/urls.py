from django.urls import path

from .views import *

urlpatterns = [
    path("", mostrar_tarefa, name="mostrar_tarefa"),
    path("create", criar_tarefa, name="criar_tarefa"),
    path("delete/<int:tarefa_id>", excluir_tarefa, name="excluir_tarefa"),
    path("update/<int:tarefa_id>", atualizar_tarefa, name="atualizar_tarefa"),
]