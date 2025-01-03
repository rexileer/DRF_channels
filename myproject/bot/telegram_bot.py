import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties

from handlers import bot_messages


API_TOKEN = 'TOKEN'
API_SERVICE_URL = 'http://127.0.0.1:8000/api/chat/llm/'

async def main():
    bot = Bot(API_TOKEN, default=DefaultBotProperties(parse_mode='HTML'))
    dp = Dispatcher()
    
    dp.include_routers(
        bot_messages.router
    )
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())