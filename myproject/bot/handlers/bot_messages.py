from aiogram import Router, F
import logging
import requests
from aiogram import types


API_SERVICE_URL = 'http://127.0.0.1:8000/api/chat/'

# Логирование
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = Router()

@router.message(F.text.lower().in_(['qu', 'q']))
async def greetings(message: types.Message):
    """
    Обработчик команды "qu" или "q".
    Отвечает пользователю приветствием.
    """
    await message.reply("Hello")
    
@router.message()
async def chat_with_llm(message: types.Message):
    user_message = message.text

    try:
        # Отправка запроса на API
        response = requests.post(API_SERVICE_URL, json={"message": user_message})
        response.raise_for_status()  # Генерирует исключение при HTTP-ошибке
        response_data = response.json()

        if response.status_code == 200:
            llm_response = response_data.get("response", "Извините, ответ отсутствует.")
            await message.answer(llm_response)
        else:
            await message.answer(f"Ошибка: {response_data.get('error', 'Неизвестная ошибка')}")

    except requests.exceptions.RequestException as e:
        logging.error(f"API request failed: {e}")
        await message.answer("Произошла ошибка при обработке вашего сообщения.")
    except ValueError as ve:
        logging.error(f"Invalid JSON response: {response.text}")
        await message.answer("Произошла ошибка при обработке вашего сообщения.")