import graphene
from graphene_django.types import DjangoObjectType
from .models import Client, Event

class ClientType(DjangoObjectType):
    class Meta:
        model = Client
        fields = ("id", "name", "cnpj", "event")

class EventType(DjangoObjectType):
    class Meta:
        model = Event
        fields = ("name", "date_init", "date_end", "hour_init", "hour_end", "location", "category")

class Query(graphene.ObjectType):
    client = graphene.Field(ClientType, id=graphene.Int())
    clients = graphene.List(ClientType)

    event = graphene.Field(EventType, id=graphene.Int())
    events = graphene.List(EventType)

    def resolve_client(self, info, id):
        try:
            return Client.objects.get(id=id)
        except Client.DoesNotExist:
            return graphene.String("Cliente nao eciste")
    
    def resolve_clients(self, info):
        return Client.objects.all()
    
    def resolve_event(self, info, id):
        return Event.objects.get(id=id)
    
    def resolve_events(self, info):
        return Event.objects.all()
    
schema = graphene.Schema(query=Query)