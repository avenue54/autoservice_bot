#handlers.py
from aiogram.fsm.state import State, StatesGroup
from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.types import Message
from config import OWNER_ID

router = Router()


class OrderForm(StatesGroup):
    waiting_for_name = State()
    waiting_for_phone = State()
    waiting_for_car_model = State() #по ТЗаданию, нужно добавить поле для модели автомобиля
    waiting_for_problem_description = State()
    
    
@router.message(Command("request"))
async def cmd_request(message: Message, state: FSMContext):
    await state.set_state(OrderForm.waiting_for_name)
    await message.answer("Как вас зовут?")
    
    
@router.message(OrderForm.waiting_for_name)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)  # сохраняем имя
    await state.set_state(OrderForm.waiting_for_phone)
    await message.answer("Ваш номер телефона?")
    
@router.message(OrderForm.waiting_for_phone)
async def process_phone(message: Message, state: FSMContext):
    await state.update_data(phone=message.text)  # сохраняем номер телефона
    await state.set_state(OrderForm.waiting_for_car_model)
    await message.answer("Модель вашего автомобиля?")
    
@router.message(OrderForm.waiting_for_car_model)
async def process_car_model(message: Message, state: FSMContext):
    await state.update_data(car_model=message.text)  # сохраняем модель автомобиля
    await state.set_state(OrderForm.waiting_for_problem_description)
    await message.answer("Опишите проблему с автомобилем.")
    
    
@router.message(OrderForm.waiting_for_problem_description)
async def process_problem(message: Message, state: FSMContext):
    await state.update_data(problem=message.text)
    
    data = await state.get_data()
    
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