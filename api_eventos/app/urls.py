from django.urls import path 
from . import views
from graphene_django.views import GraphQLView
from app.schema import schema  

urlpatterns = [

    path('event/', views.get_event),
    path('events/', views.events),
    path('event/<int:pk>', views.show_event),
    path('event/create/', views.post_event), 
    path('event/update/<int:pk>', views.put_event), 
    path('event/delete/<int:pk>', views.delete_event), 
    #Start client Urls. 
    path('client/', views.get_client),
    path('client/<int:pk>', views.show_client),  
    path('client/create/', views.post_client),
    path('client/update/<int:pk>', views.put_client),
    path('client/delete/<int:pk>', views.delete_client), 
    #GraphQl route 
    path("graphql", GraphQLView.as_view(graphiql=True, schema=schema)),

]