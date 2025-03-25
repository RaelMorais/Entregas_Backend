from rest_framework import serializers
from .models import Client, Event, Place, Category


'''
Serializers que serão usados para Post, Put, Delete
SerializerEvent() -> Retornar todos os itens da tabela de eventos. 
SerializerClient() -> Retornar todos os itens da tabela de cliente. 

'''
class SerializerEvent(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class SerializerClient(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

'''
Serializers para Get para retornar o nome na Urls /events/ e clients/ e não o Id.
Por padrão, quando renderiza todos os objetos, o Django retorna Fks com seu Id e não nome. 
'''
class getEventSerializer(serializers.ModelSerializer):
    ''' Serializer para buscar um valor especifico no banco invés de seu ID. Fields = ['name'] é o campo que estou buscando. '''
    class Meta:
        model = Event
        fields = ['name'] 

class ClientSerializer(serializers.ModelSerializer):
    '''Serializer para retornar os detalhes do cliente, e invés de retornar o ID na coluna events, irá retornar o evento que o cliente está relacionado.'''
    event = serializers.SerializerMethodField()

    class Meta:
        model = Client
        fields = ['name', 'cnpj', 'event'] #Campos serializados. 

    def get_event(self, obj): #Função para o nome do evento 
        return obj.event.name

class LocationSerializer(serializers.ModelSerializer):
    '''Função para retornar o nome da localização invés de seu ID '''
    class Meta:
        model = Place
        fields = ['name_place'] #Campo que será serializado, neste caso retornará o nome da localização. 

class Category(serializers.ModelSerializer):
    '''Para retornar o nome da categoria invés de seu ID'''
    class Meta:
        model = Category
        fields = ['name_category']


class EventSerializer(serializers.ModelSerializer):
    '''Serializer onde retornara os dados da tabela Events'''
    location = serializers.SerializerMethodField() #Serializer para retornar o nome da localização. 
    category = serializers.SerializerMethodField() #Serializer para retornar o nome da categoria. 

    class Meta:
        model = Event
        fields = ['name', 'date_init', 'date_end', 'hour_init', 'hour_end', 'location', 'category']

    '''Função para retornar o nome da categoria e localização '''
    def get_location(self, obj): 
        return obj.location.name_place
    def get_category(self,obj):
        return obj.category.name_category