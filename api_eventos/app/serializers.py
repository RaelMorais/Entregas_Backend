from rest_framework import serializers
from .models import Client, Event, Place, Category



class SerializerEvent(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class SerializerClient(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'







'''
Serializers para Get aparecendo o nome. 




'''
class getEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['name'] 

class ClientSerializer(serializers.ModelSerializer):
    event = serializers.SerializerMethodField()

    class Meta:
        model = Client
        fields = ['name', 'cnpj', 'event']

    def get_event(self, obj): #Função para retornar o nome da categoria e localização 
        return obj.event.name

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['name_place']  

class Category(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name_category']


class EventSerializer(serializers.ModelSerializer):
    
    location = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ['name', 'date_init', 'date_end', 'hour_init', 'hour_end', 'location', 'category']
        
    def get_location(self, obj): #Função para retornar o nome da categoria e localização 
        return obj.location.name_place
    def get_category(self,obj):
        return obj.category.name_category