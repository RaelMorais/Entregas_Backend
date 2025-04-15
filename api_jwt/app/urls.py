from django.urls import path
from . import views  
from .views import *

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('create/', view=views.create_user, name="Create User"),
    path('login/', view=views.login_user, name='Login User'),
    path('read/', view=views.root, name="Read Data"),
    path('generic/<int:pk>', PutDeleteClass.as_view()),

        # URL para obter o token JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # URL para atualizar o token JWT
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]