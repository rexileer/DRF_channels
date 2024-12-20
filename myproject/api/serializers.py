from rest_framework import serializers

class ChatMessageSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=500)  # Входящее сообщение
    response = serializers.CharField(max_length=500, read_only=True)  # Ответ (только для чтения)
