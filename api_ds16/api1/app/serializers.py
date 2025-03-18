from rest_framework import serializers
from .models import Car


class CarSerializer(serializers.ModelSerializer):
    #Define a classe de serialização para o modelo Car
    class Meta: 
        model = Car #Especifica o modelo que será usado
        fields = '__all__' #Inclui todos os campos do modelo no serializer