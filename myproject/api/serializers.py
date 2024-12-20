from rest_framework import serializers
from core.models import ChatMessage


class ChatMessageSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=500)  # Входящее сообщение
    response = serializers.CharField(max_length=500, read_only=True)  # Ответ (только для чтения)


class ChatHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = ['user_message', 'llm_response', 'created_at']
