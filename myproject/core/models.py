from django.db import models

# Create your models here.
class ChatMessage(models.Model):
    user_message = models.TextField()  # Сообщение пользователя
    llm_response = models.TextField()  # Ответ от LLM
    created_at = models.DateTimeField(auto_now_add=True)  # Время создания

    def __str__(self):
        return f"Message at {self.created_at}"
