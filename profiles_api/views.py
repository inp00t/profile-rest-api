from rest_framework.views import APIView
from rest_framework.response import Response


class HellloApiView(APIView):
    """Test API View"""
    def get(self, request, format=None):
        """Return a list of APIView features"""
        an_apiview = [
        'Uses HTTP methods as function(get, post, path, put, delete)'
        'Is similar to a tradicional Django View',
        'Gives you the most control over you application logic',
        'Is mapped manually to URLs',
        ]

        return Response({'message': 'hello,', 'an_apiview': an_apiview})
