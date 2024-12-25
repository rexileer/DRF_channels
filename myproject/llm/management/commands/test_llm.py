from django.core.management.base import BaseCommand
from groq import Groq
from django.conf import settings

class Command(BaseCommand):
    help = "Тестирование базовой функциональности LLM через Groq"

    def handle(self, *args, **kwargs):
        # Проверяем ключ
        if not settings.GROQ_API_KEY:
            self.stdout.write(self.style.ERROR("GROQ_API_KEY не задан в настройках."))
            return

        # Инициализация клиента
        client = Groq(api_key=settings.GROQ_API_KEY)
        dialog_history = []

        # Основной цикл
        while True:
            user_input = input("Введите ваше сообщение ('stop' для завершения): ")
            if user_input.lower() == "stop":
                break

            # Добавляем сообщение пользователя
            dialog_history.append({
                "role": "user",
                "content": user_input,
            })

            models = ["gemma-7b-it", "llama3-70b-8192", "llama3-8b-8192", "mixtral-8x7b-32768"]
            try:
                # Отправляем запрос
                chat_completion = client.chat.completions.create(
                    messages=dialog_history,
                    model=models[1],
                )

                response = chat_completion.choices[0].message.content
                self.stdout.write(self.style.SUCCESS(f"Ответ модели: {response}"))

                # Добавляем ответ модели
                dialog_history.append({
                    "role": "assistant",
                    "content": response,
                })

            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Ошибка: {str(e)}"))
