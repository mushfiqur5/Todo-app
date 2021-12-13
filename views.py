from django.shortcuts import render
import rest_framework
from rest_framework import request
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TodoSerializer
from .models import Todo
from rest_framework import status
from rest_framework import response,serializers
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TodoSerializer
from .models import Todo
from rest_framework import status
from rest_framework import response,serializers
from django.shortcuts import get_object_or_404
# from .utils import getItemList,createItem,getItemDetail,updateItem,deleteItem

# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    
    routes = [
        {
            'Endpoint': '/items',
            'method': 'GET',
            'body':None,
            'description':'Returns an array of notes'
        },
        {
            'Endpoint': '/items/id',
            'method': 'GET',
            'body':None,
            'description':'Returns a single note object'
        },
        {
            'Endpoint': '/items/create',
            'method': 'POST',
            'body':{'body':""},
            'description':'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/items/id/update',
            'method': 'PUT',
            'body':None,
            'description':'Returns an array of notes'
        },
        {
            'Endpoint': '/items/id/delete',
            'method': 'DELETE',
            'body':None,
            'description':'Deletes an existing note'
        },
    ]
    return Response(routes)

@api_view(['GET'])
def getItems(request):
    items=Todo.objects.all()
    serializer=TodoSerializer(items,many=True)
    return Response(serializer.data)

@api_view(['GET'])

def getItem(request,id):
    items = Todo.objects.get(id=id)
    serializer = TodoSerializer(items,many=False)
    return Response(serializer.data)


@api_view(['POST'])

def createItem(request):
    serializer=TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
    #code that was in tuto--------------
    # data=request.data
    # item= Todo.objects.create(
    #     body=data['body']
    # )
    # serializer = TodoSerializer(item,many=False)
    # return Response(serializer.data)
    
@api_view(['PUT'])
def updateItem(request,id):
    data = request.data
    item = Todo.objects.get(id=id)
    serializer = TodoSerializer(instance=item,data=data)
    
    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteItem(request,id):
    item = Todo.objects.get(id=id)
    item.delete()
    return Response('Item was deleted')