from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.viewsets import ViewSet

@api_view(['GET'])
def simple_view(request):
    return Response({'message': 'Simple endpoint'})

@api_view(['GET'])
def test_view(request):
    return Response({'message': 'DRF is working!'})


    

class ExampleViewSet(ViewSet):
    def list(self, request):
        return Response({'message': 'List of examples'})
    
    def create(self, request):
        return Response({'message': 'Example created'})
    
    def retrieve(self, request, pk=None):
        return Response({'message': f'Example {pk}'})
    