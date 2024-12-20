from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('chat/', views.chat, name='chat'),
    path('chat-test/', views.chat_logic, name='chat_test'),
]
