from rest_framework import serializers
from .models import Carro, Piloto

# Serializador para o modelo Carro
class CarroSerializer(serializers.ModelSerializer):
    # Se precisar adicionar lógica customizada, pode ser feito aqui.
    class Meta:
        model = Carro
        fields = '__all__'  # Inclui todos os campos do modelo Carro no serializer

# Serializador para o modelo Piloto
class PilotoSerializer(serializers.ModelSerializer):
    # Aqui, você pode adicionar lógica adicional para validar ou personalizar a serialização dos campos, se necessário.
    class Meta:
        model = Piloto
        fields = '__all__'  # Inclui todos os campos do modelo Piloto no serializer
