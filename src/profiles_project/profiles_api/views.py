from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    #Test API View.

    def get(self, request, format=None):
        #Returns a list of API features

        an_apiview =[
            'Uses HTTP methods as function (get, post, patch, put, delete',
            'It is similar to a tradional Django View.',
            'Gives you the most control over the logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message':'Hello!!', 'an_apiview':an_apiview})