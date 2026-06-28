#handlers.py
from aiogram.fsm.state import State, StatesGroup
from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command, StateFilter
from aiogram.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from config import OWNER_ID
from aiogram import F
import re
from database import save_request


router = Router()

button_main = KeyboardButton(text="📝 Оставить заявку")
keyboard = ReplyKeyboardMarkup(keyboard=[[button_main]], resize_keyboard=True)
cancel_button = KeyboardButton(text="❌ Отменить")
cancel_keyboard = ReplyKeyboardMarkup(keyboard=[[cancel_button]], resize_keyboard=True)

def is_valid_phone(phone: str) -> bool:
    pattern = r'^\+7[\s\-]?\(?\d{3}\)?[\s\-]?\d{3}[\s\-]?\d{2}[\s\-]?\d{2}$'
    return bool(re.match(pattern, phone))

class OrderForm(StatesGroup):
    waiting_for_name = State()
    waiting_for_phone = State()
    waiting_for_car_model = State() #по ТЗаданию, нужно добавить поле для модели автомобиля
    waiting_for_problem_description = State()

@router.message(F.text == "❌ Отменить", StateFilter(
    OrderForm.waiting_for_name,
    OrderForm.waiting_for_phone,
    OrderForm.waiting_for_car_model,
    OrderForm.waiting_for_problem_description
))
async def cancel_order(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("В следующий раз!", reply_markup=keyboard)

 
@router.message(F.text == "📝 Оставить заявку")
async def btn_request(message: Message, state: FSMContext):
    await state.set_state(OrderForm.waiting_for_name)
    await message.answer("Как вас зовут?", reply_markup=cancel_keyboard)
    
    
@router.message(OrderForm.waiting_for_name)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)  # сохраняем имя
    await state.set_state(OrderForm.waiting_for_phone)
    await message.answer("Ваш номер телефона в формате +7XXXXXXXXXX")
    
@router.message(OrderForm.waiting_for_phone)
async def process_phone(message: Message, state: FSMContext):
    if not is_valid_phone(message.text):  # ← сначала проверяем
        await message.answer("❌ Неверный формат. Введите номер в формате +7XXXXXXXXXX")
        return  # ← выходим, состояние не меняется
    
    await state.update_data(phone=message.text)  # сохраняем только если номер верный
    await state.set_state(OrderForm.waiting_for_car_model)
    await message.answer("Марка и модель вашего автомобиля?", reply_markup=cancel_keyboard)
    
@router.message(OrderForm.waiting_for_car_model)
async def process_car_model(message: Message, state: FSMContext):
    await state.update_data(car_model=message.text)  # сохраняем модель автомобиля
    await state.set_state(OrderForm.waiting_for_problem_description)
    await message.answer("Опишите проблему с автомобилем.", reply_markup=cancel_keyboard)


@router.message(OrderForm.waiting_for_problem_description)
async def process_problem(message: Message, state: FSMContext):
    await state.update_data(problem=message.text)
    
    data = await state.get_data()
    
    await save_request(
    name=data['name'],
    phone=data['phone'],
    brand=data['car_model'],
    problem=data['problem']
    )
    
    order_text = (
        f"📋 Новая заявка!\n\n"
        f"👤 Имя: {data['name']}\n"
        f"📞 Телефон: {data['phone']}\n"
        f"🚗 Автомобиль: {data['car_model']}\n"
        f"🔧 Проблема: {data['problem']}"
    )
    
    await message.bot.send_message(OWNER_ID, order_text)
    await message.answer("✅ Заявка принята! Мы свяжемся с вами.")
    await state.clear()