from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Event, Client, Place, Category
from django.utils import timezone
from datetime import timedelta
from rest_framework import status
from .serializers import EventSerializer, ClientSerializer, SerializerEvent, SerializerClient
from datetime import datetime


@api_view(['GET'])
def get_event(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def show_event(request, pk):
    try:
        event = Event.objects.get(pk=pk)
    except Event.DoesNotExist:
        return Response({'Error':'Event does not exist'}, status=status.HTTP_404_NOT_FOUND)
    serializer = EventSerializer(event)
    return Response(serializer.data)

@api_view(['POST'])
def post_event(request):
    if request.method == 'POST':
        serializer = SerializerEvent(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT'])
def put_event(request, pk):
    try:
          event = Event.objects.get(pk=pk)
    except event.DoesNotExist:
        return Response({'erro':'Event Doenst exist'}, status=status.HTTP_404_NOT_FOUND)
     
    serializer = SerializerEvent(event,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
  
@api_view(['DELETE'])
def delete_event(request, pk):
    try:
          event = Event.objects.get(pk=pk)
    except Event.DoesNotExist:
        return Response({'erro':'Event Doenst exist'}, status=status.HTTP_404_NOT_FOUND)
    event.delete()
    return Response({'message': 'Event delete sucefull'}, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_client(request):
    clients = Client.objects.all()
    serializer = ClientSerializer(clients, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def show_client(request, pk):
    try:
        client = Client.objects.get(pk=pk)
    except Client.DoesNotExist:
        return Response({'Error':'Client does not exist'}, status=status.HTTP_404_NOT_FOUND)
    serializer = ClientSerializer(client)
    return Response(serializer.data)


@api_view(['POST'])
def post_client(request):
    if request.method == 'POST':
        serializer = SerializerClient(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Client Created')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT'])
def put_client(request, pk):
    try:
          client = Client.objects.get(pk=pk)
    except Client.DoesNotExist:
        return Response({'erro':'Client Doenst exist'}, status=status.HTTP_404_NOT_FOUND)
     
    serializer = SerializerClient(client,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
  
@api_view(['DELETE'])
def delete_client(request, pk):
    try:
          client = Client.objects.get(pk=pk)
    except Event.DoesNotExist:
        return Response({'erro':'Client Doenst exist'}, status=status.HTTP_404_NOT_FOUND)
    client.delete()
    return Response({'message': 'Client delete sucefull'}, status=status.HTTP_200_OK)

@api_view(['GET'])
def events(request):
    info = Event.objects.all()
    categoria = request.query_params.get('categoria')
    if categoria:
        try:
            category = Category.objects.get(name_category__icontains=categoria)
            info = info.filter(category=category)
            if not info.exists():
                return Response("Categoria inexistente", status=404)
        except Category.DoesNotExist:
            return Response("Category not found", status=404)
        
    data = request.query_params.get('data')
    if data:
        try:
            data_format = datetime.strptime(data, "%Y-%m-%d").date()#Transforma a data fornecida no formato correto
            info = info.filter(date_init=data_format)
            if not info.exists():
                return Response("Sem dados cadastrados")
        except ValueError:
            return Response("Invalid date format, use YYYY-MM-DD", status=400)



    # Limitar a quantidade de resultados
    quantidade = request.query_params.get('quantidade')
    if quantidade:
        try:
            # Limita o número de resultados
            info = info[:int(quantidade)]
            if not info.exists():
                return Response(ModuleNotFoundError)
        except ValueError:
            return Response("Quantidade deve ser um número inteiro", status=400)

    # Ordenação
    ordenacao = request.query_params.get('ordenacao')
    if ordenacao:
        if ordenacao == 'data':
            info = info.order_by('date_init')
        else:
            return Response("Ordenação inválida. Use 'data'.", status=400)

    serializer = EventSerializer(info, many=True)
    return Response(serializer.data)

# Create your views here.
