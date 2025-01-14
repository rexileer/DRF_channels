from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.viewsets import ViewSet
from rest_framework.views import APIView
from rest_framework import status
from .serializers import ChatMessageSerializer
from core.models import ChatMessage
from rest_framework.generics import ListAPIView
from .serializers import ChatHistorySerializer
from llm.llm_logic import process_message



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
    Чат API с интеграцией LLM
    """

    def post(self, request, *args, **kwargs):
        serializer = ChatMessageSerializer(data=request.data)
        if serializer.is_valid():
            user_message = serializer.validated_data['message']
            
            # Извлечение истории чата
            dialog_history = [
                {"role": "user", "content": msg.user_message} if msg.user_message else
                {"role": "assistant", "content": msg.llm_response}
                for msg in ChatMessage.objects.all().order_by("created_at")
            ]

            # Генерация ответа через LLM
            response_message = process_message(user_message, dialog_history)
            
            # Сохранение сообщения и ответа в БД
            ChatMessage.objects.create(
                user_message=user_message,
                llm_response=response_message
            )

            return Response(
                {"message": user_message, "response": response_message},
                status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChatHistoryAPIView(ListAPIView):
    """
    API для получения истории чата.
    """
    queryset = ChatMessage.objects.all().order_by('created_at')
    serializer_class = ChatHistorySerializer


class ClearChatAPIView(APIView):
    """
    API для очистки истории чата.
    """
    def delete(self, request, *args, **kwargs):
        ChatMessage.objects.all().delete()  # Удаляем все сообщения
        return Response({"message": "Chat history cleared."}, status=status.HTTP_200_OK)
