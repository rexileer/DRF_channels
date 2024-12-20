from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'example', views.ExampleViewSet, basename='example')

urlpatterns = [
    path('test/', views.test_view, name='test_view'),
    path('', include(router.urls)),
    path('simple-endpoint/', views.simple_view, name='simple_endpoint'),
    path('chat/', views.ChatAPIView.as_view(), name='chat_api'),
    path('chat/history/', views.ChatHistoryAPIView.as_view(), name='chat_history'),
    path('chat/clear/', views.ClearChatAPIView.as_view(), name='chat_clear'),
]
