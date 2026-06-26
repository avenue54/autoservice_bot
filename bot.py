# bot.py
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession
from config import BOT_TOKEN
from aiogram.filters import Command
from handlers import router


session = AiohttpSession(proxy="http://127.0.0.1:10809")
bot = Bot(token=BOT_TOKEN, session=session)
dp = Dispatcher()

@dp.message(Command("start"))  # ← реагирует ТОЛЬКО на /start
async def cmd_start(message):
    await message.answer(
        "Добро пожаловать в автосервис! 🚗\n\n"
        "Я помогу вам оставить заявку на ремонт.\n"
        "Напишите /request чтобы начать."
    )

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


asyncio.run(main())