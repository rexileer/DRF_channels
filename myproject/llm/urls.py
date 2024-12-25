from django.urls import path
from . import views

urlpatterns = [
    # path("chat/", LLMChatAPIView.as_view(), name="llm-chat"),
    path("response/", views.llm_response, name="llm_response") 
]
