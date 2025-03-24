from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Event, Client, Place, Category
from django.utils import timezone
from datetime import timedelta
from rest_framework import status
from .serializers import EventSerializer, ClientSerializer, SerializerEvent, SerializerClient

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
     
    serializer = SerializerEvent(client,data=request.data)
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
    now = timezone.now().date()
    next_days = now + timedelta(days=7)
    events = Event.objects.filter(date_init__lte=next_days, date_init__gte=now)
    quantity = request.GET.get('quantity')
    category = request.GET.get('category')
    ordering = request.GET.get('ordering')
    data = request.GET.get('data')
    
    if category and Category.objects.filter(name_category=category).exists():
            events = events.filter(category__name_category=category)
    elif category:
            return Response ("Category not found")

    
    if data:
            events = events.filter(date_init=data)
            if not events.exists():
                return Response("Data Not found")
    
    if quantity:
            try:
                events = events[:int(quantity)]
            except ValueError:
                return Response ("response do capeta")
            
   
    if ordering == 'data':
         events = events.order_by('date_init')
    elif ordering:
         return Response('Invalid')

    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)
   
# Create your views here.
