from rest_framework.views import APIView                                        # Imports APIView class from REST framework.
from rest_framework.response import Response                                    # Is used to return responses from the APIView. It is a standard response object that when you call
                                                                                # the APIView or when Django REST Framework calls our APIView it is expecting it to return this standard
                                                                                # response object.
from rest_framework import status                                               # Imports status instructions.
from profiles_api import serializers                                            # Imports serializers.py from profiles_api app.

from rest_framework import viewsets
from profiles_api import models

from rest_framework import filters

from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions


class HelloApiView(APIView):                                                    # It creates a new class based on the APIView class that Django REST Framework provides and it allows
    """Test API View"""                                                         # us to define the application logic for our endpoint that we are going to assign to this view.
                                                                                # So the way it works is you define a URL (whitch is our endpoint) and then you assign it to this view
                                                                                # and the Django REST Framework handles it by calling the appropriate function in the view for the HTTP
                                                                                # request that you make.

    serializer_class = serializers.HelloSerializer                              # Adds serializer class to the HelloApiView class.

    def get(self, request, format = None):                                      # To accept the HTTP GET request to our API. It is typically used to retrieve a list of objects
        """Returns a list of APIView features"""                                # or a specific object.
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message':'Hello!', 'an_apiview':an_apiview})          # It converts the response object to json. In order to convert it to json it needs to be either
                                                                                # a list or adictionary.
    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data = request.data)                 # Retrieve the serializer and pass in the daa that was sent in request.
                                                                                # This is a standard way to retrieve the serializer_class when working with serializers in a view.
        if serializer.is_valid():                                               # Check serializers.py to see requirements that the serializer must meet.
            name = serializer.validated_data.get('name')                        # Retrieves the name from validated data.
            message = 'Hello {}'.format(name)                                   # Creates a "hello" message.
            return Response({'message' : message})                              # Returns validated response.
        else:
            return Response(
                            serializer.errors,
                            status = status.HTTP_400_BAD_REQUEST
                            )                                                   # Returns error response with error 400 status.

    def put(self, request, pk = None):
        """Handle updating an object"""
        return Response({'method' : 'PUT'})

    def patch(seld, request, pk = None):
        """Handle a partial update of an object"""
        return Response({'method' : 'PATCH'})

    def delete(self, request, pk = None):
        """Delete an object"""
        return Response({'method' : 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):                                                    # Notice that it is the same syntax as we added to post function in HelloApiView class.
        """Return a 'hello' message"""
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message' : 'Hello!', 'a_viewset' : a_viewset})

    def create(self, request):
        """Create a new 'hello' message"""
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = 'Hello {}'.format(name)
            return Response({'message' : message})
        else:
            return Response(
                    serializer.errors,
                    status = status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk = None):
        """Handle getting an object by its ID"""
        return Response({'http_method' : 'GET'})

    def update(self, request, pk = None):
        """Handle updating an object"""
        return Response({'http_method' : 'PUT'})

    def partial_update(self, request, pk = None):
        """Handle updating part od an object"""
        return Response({'http_method' : 'PATCH'})

    def destroy(self, request, pk = None):
        """Handle removing an object"""
        return Response({'http_method' : 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):                                # Creates a new Model ViewSet
    """Handle creating and updating profiles"""                                 # The way you use a Model ViewSet is you connect it up to a serializer class just like you would
                                                                                # a regular ViewSet and you provide a queryset to the Model ViewSet so it knows which objects in
                                                                                # the database are going to be managed through this ViewSet.
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()                                 # The Django REST Framework knows the standard functions that you would want to perform on a Model ViewSet
                                                                                # and that is the create function to create new items, the list function to list the models that are in
                                                                                # the database, the update, partial update and destroy to manage specific model objects in the database.
                                                                                # Django REST Framework takes care of all of this for us just by assigning the serializer class to
                                                                                # a model serializer and the queryset. This is the great thing about the Model ViewSet.
    authentication_classes = (TokenAuthentication,)                             # remember to add a comma after token authentication so that this gets created as a tuple instead of
                                                                                # just a single item. You can configure one or more types of authentication with a particular ViewSet
                                                                                # in the Django REST Framework. The way it works is you just add all the authentication classes to this
                                                                                # authentication_classes class variable.
    permission_classes = (permissions.UpdateOwnProfile,)                        # Sets how the user gets permission to do certain things.
    filter_backends = (filters.SearchFilter,)                                   # Adds a filter backend. You can add one or more filter backends to a particular ViewSet.
    search_fields = ('name', 'email',)                                          # This tells the filter backend which fields we are going to make searchable by this filter.
