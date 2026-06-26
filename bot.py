# bot.py
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession
from config import BOT_TOKEN
from aiogram.filters import Command
from handlers import router
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



session = AiohttpSession(proxy="http://127.0.0.1:10809")
bot = Bot(token=BOT_TOKEN, session=session)
dp = Dispatcher()

button = KeyboardButton(text="📝 Оставить заявку")
keyboard = ReplyKeyboardMarkup(keyboard=[[button]], resize_keyboard=True)

@dp.message(Command("start"))  # ← реагирует ТОЛЬКО на /start
async def cmd_start(message):
    await message.answer(
        "Добро пожаловать в автосервис! 🚗\n\n"
        "Я помогу вам оставить заявку на ремонт.\n"
        "Нажмите на кнопку ниже, чтобы начать запонять заявку.", reply_markup=keyboard)

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


asyncio.run(main())
