from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.



@api_view(['get'])
def hellow_world(r):
    return Response({
        "message":"hellow world",
        })


@api_view(['post','get'])
def welcome(r):
    if r.method =='GET':
        return Response({
                "message":"hellow world",
                })
    if r.method =='POST':
        return Response({
            "message":"hello {}".format(r.data["name"])
        })