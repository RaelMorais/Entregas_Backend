from django.urls import path
from . import views  
from .views import *


urlpatterns = [
    path('create/', view=views.create_user, name="Create User"),
    path('login/', view=views.login_user, name='Login User'),
    path('read/', view=views.root, name="Read Data"),
    path('generic/<int:pk>', PutDeleteClass.as_view()),

]