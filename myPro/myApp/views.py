from django.shortcuts import render

from rest_framework.decorators import api_view 
from rest_framework.response import Response 


@api_view(['GET'])
def hello_world(request):
    return Response({'message': 'Hello, World!'})

@api_view(['POST' , 'GET'])
def hell(request):
    if request.method == 'GET':
        return Response({'message': 'Hello, World'})
    elif request.method == 'POST':
        return Response({'message': 'hello {}'.format(request.data["name"])})