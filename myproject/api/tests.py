from rest_framework.test import APITestCase
from rest_framework import status
from core.models import ChatMessage

class ChatApiTests(APITestCase):
    def setUp(self):
        # Создадим несколько сообщений для теста
        ChatMessage.objects.create(user_message="Hello", llm_response="Hi there!")
        ChatMessage.objects.create(user_message="How are you?", llm_response="I'm fine, thanks!")

    def test_send_message(self):
        """
        Проверка отправки сообщения через API.
        """
        url = '/api/chat/'
        data = {'message': 'What is the weather like today?'}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('response', response.data)  # Убедимся, что есть поле 'response' в ответе

    def test_chat_history(self):
        """
        Проверка получения истории чата через API.
        """
        url = '/api/chat/history/'
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Должно быть два сообщения в истории
        self.assertEqual(response.data[0]['user_message'], "Hello")  # Первое сообщение должно быть "Hello"
        self.assertEqual(response.data[1]['llm_response'], "I'm fine, thanks!")  # Второе сообщение должно иметь ответ "I'm fine, thanks!"
