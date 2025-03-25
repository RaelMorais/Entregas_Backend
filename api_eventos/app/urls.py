from django.urls import path 
from . import views
from graphene_django.views import GraphQLView
from app.schema import schema  

urlpatterns = [
    #Events urls. 
    path('event/', views.get_event),#Event Urls for all events with Category name and Location Name
    path('events/', views.events), #Event operations with Query parameters. 
    path('event/<int:pk>', views.show_event), #Serach Event by especific Id
    path('event/create/', views.post_event), #urls for Create event 
    path('event/update/<int:pk>', views.put_event), #Urls for update by id event 
    path('event/delete/<int:pk>', views.delete_event), #Urls for delete by id event 
    #Start client Urls. 
    path('client/', views.get_client), #Client urls for show all clients with Event name 
    path('client/<int:pk>', views.show_client),  #Client url for especific client search 
    path('client/create/', views.post_client), #Url for a Create operation 
    path('client/update/<int:pk>', views.put_client), #Url for a update client by ID
    path('client/delete/<int:pk>', views.delete_client), #url for a delete client by Id. 
    #GraphQl route 
    path("graphql", GraphQLView.as_view(graphiql=True, schema=schema)), #grapql route 

]