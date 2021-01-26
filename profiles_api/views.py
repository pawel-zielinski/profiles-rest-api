from rest_framework.views import APIView                                        # Imports APIView class from REST framework.
from rest_framework.response import Response                                    # Is used to return responses from the APIView. It is a standard response object that when you call
                                                                                # the APIView or when Django REST Framework calls our APIView it is expecting it to return this standard
                                                                                # response object.
class HelloApiView(APIView):                                                    # It creates a new class based on the APIView class that Django REST Framework provides and it allows
    """Test API View"""                                                         # us to define the application logic for our endpoint that we are going to assign to this view.
                                                                                # So the way it works is you define a URL (whitch is our endpoint) and then you assign it to this view
                                                                                # and the Django REST Framework handles it by calling the appropriate function in the view for the HTTP
                                                                                # request that you make.


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
