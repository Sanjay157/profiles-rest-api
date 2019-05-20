from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status        #contains a list of HTTP Status response like 404, 505, 400

from . import serializers


# Create your views here.

class HelloApiView(APIView):
    #Test API View.

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        #Returns a list of API features

        an_apiview =[
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'It is similar to a tradional Django View.',
            'Gives you the most control over the logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message':'Hello!!', 'an_apiview':an_apiview}) 

    def post(self, request):
        """Create a hello message with our name."""

        serializer = serializers.HelloSerializer(data=request.data)         #now the data will contain all the variabe in HelloSerializer class

        if serializer.is_valid():
            name = serializer.data.get('name')              #to retrieve 'name' field from data and assigning to variable called 'name'
            message = 'Hello {0}'.format(name)
            return Response({'message':message})
        
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):            #pk: Primary key
        """Handles updating an object."""

        return Response({'method':'put'})

    def patch(self, request, pk=None):
        """Patch request, only updates fields provided in the request."""

        return Response({'method':'patch'})
        

    def delete(self, request, pk=None):
        """Deletes an object"""

        return Response({'method':'delete'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet."""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial update, destroy)',
            'Automatically maps to URL using Routers',
            'Provides more functionality with less code.'
        ]

        return Response({'message':'Hello!', 'a_viewset':a_viewset})

    def create(self, request):
        """Create a new hello message with our name."""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
             name = serializer.data.get('name')
             message= 'Hello {0}'.format(name)
             return Response({'message':message})

        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handles getting an object by its ID"""

        return Response({'http_method': 'GET'})
    
    def update(self, request, pk=None):
        """Handles updating an object"""

        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        """Partially updates the Objects"""

        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk=None):
        """Handles deleting an Object"""

        return Response({'http_method':'DELETE'})

