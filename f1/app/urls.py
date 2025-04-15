from django.urls import path
from .views import * 
from . import views
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="API da Fórmula 1",
        default_version='v1',
        description="Documentação da API para dados da Fórmula 1"
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   path("piloto/", views.GetPostPiloto.as_view()),
   path('carro/', views.GetPostCarro.as_view()),
   path('piloto/<int:pk>', views.PilotoUpdateDelete.as_view()),
   path('carro/<int:pk>', views.PilotoUpdateDelete.as_view()),
   path('redoc/', view=schema_view.with_ui('redoc', cache_timeout=0)),
   path('doc/', view=schema_view.with_ui('swagger', cache_timeout=0)),
]
