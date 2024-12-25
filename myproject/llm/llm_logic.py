from groq import Groq
from django.conf import settings

# Инициализация клиента LLM
client = Groq(api_key=settings.GROQ_API_KEY)

def process_message(user_message: str, dialog_history: list) -> str:
    """
    Обрабатывает сообщение пользователя с помощью LLM.

    :param user_message: Сообщение пользователя.
    :param dialog_history: История диалога.
    :return: Ответ от модели.
    """
    # Добавляем сообщение пользователя в историю
    dialog_history.append({
        "role": "user",
        "content": user_message,
    })

    # Выбор модели
    models = ["gemma-7b-it", "llama3-70b-8192", "llama3-8b-8192", "mixtral-8x7b-32768"]

    # Отправка сообщения в LLM
    chat_completion = client.chat.completions.create(
        messages=dialog_history,
        model=models[1],  # Используем модель llama3-70b-8192
    )

    # Ответ модели
    response = chat_completion.choices[0].message.content

    # Добавляем ответ модели в историю
    dialog_history.append({
        "role": "assistant",
        "content": response,
    })

    return response

# def process_message(user_message: str) -> str:
#     """
#     Обрабатывает сообщение пользователя с помощью LLM.
#     Для теста пока возвращает фиксированный ответ.

#     :param user_message: Сообщение пользователя.
#     :return: Ответ от модели.
#     """
#     # Здесь будет подключение к LLM, например через API или локальную библиотеку.
#     return f"Echo: {user_message}"  # Пока что простой ответ
