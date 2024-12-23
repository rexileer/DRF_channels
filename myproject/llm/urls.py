from django.urls import path
from .views import LLMChatAPIView

urlpatterns = [
    path("chat/", LLMChatAPIView.as_view(), name="llm-chat"),
]
