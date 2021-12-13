from re import L
from rest_framework import serializers
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer

def getItemList(request):
    items = Todo.objects.all()
    serializer = TodoSerializer(items,many=True)
    return Response(serializer.data)

def getItemDetail(request,pk):
    items = Todo.objects.get(id=pk)
    serializer = TodoSerializer(items,many=False)
    return Response(serializer.data)

def createItem(request):
    data = request.data
    note = Todo.objects.create(
        body=data['body']
    )
    serializer = TodoSerializer(note, many=False)
    return Response(serializer.data)


