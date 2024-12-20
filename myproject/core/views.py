from django.shortcuts import render
from django.http import JsonResponse
from llm.llm_logic import process_message


def index(request):
    return render(request, 'core/index.html')


def chat(request):
    return render(request, 'core/chat.html')


def chat_logic(request):
    """
    Тестовый эндпоинт для проверки работы логики чата.
    """
    user_message = request.GET.get('message', '')
    if not user_message:
        return JsonResponse({'error': 'No message provided'}, status=400)

    response = process_message(user_message)
    return JsonResponse({'user_message': user_message, 'response': response})
