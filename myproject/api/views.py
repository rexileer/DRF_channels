from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.viewsets import ViewSet
from rest_framework.views import APIView
from rest_framework import status
from .serializers import ChatMessageSerializer
from core.models import ChatMessage



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


class ChatAPIView(APIView):
    """
    Эхо-чат API
    """
    def post(self, request, *args, **kwargs):
        serializer = ChatMessageSerializer(data=request.data)
        if serializer.is_valid():
            user_message = serializer.validated_data['message']
            # Логика обработки сообщения (пока эхо-ответ)
            response_message = f"Echo: {user_message}"
            
            ChatMessage.objects.create(
                user_message=user_message,
                llm_response=response_message
            )

            return Response({"message": user_message, "response": response_message}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
