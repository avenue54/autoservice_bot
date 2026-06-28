# 🚗 AutoService Telegram Bot

<p align="center">
  <a href="#-english">English</a> •
  <a href="#-русский">Русский</a>
</p>

# 🇬🇧 English

A Telegram bot for receiving car repair requests from customers and automatically sending them to the service owner.

---

## 📖 Description

**AutoService Telegram Bot** helps auto repair shops automate the process of receiving customer requests.

The bot collects all the necessary information from the customer and instantly sends a formatted request to the service owner.

---

## ✨ Features

- 🚀 `/start` — Welcome message
- 📝 Create a new repair request via button
- 👤 Collect customer's name
- 📞 Collect phone number with validation
- 🚗 Collect car make and model
- 🔧 Collect problem description
- 📨 Send the completed request to the owner
- ❌ Cancel request at any time
- 💾 Save requests to SQLite database

---

## 💬 Example

### Customer
Name: Daniel

Phone: +79001234567

Car: Lada Vesta

Problem: Engine won't start

### Owner receives
📋 New Request
👤 Name: Daniel

📞 Phone: +79001234567

🚗 Car: Lada Vesta

🔧 Problem: Engine won't start

---

## 🛠 Technologies

- Python
- aiogram
- aiosqlite
- python-dotenv
- aiohttp-socks

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/avenue54/autoservice_bot.git
cd autoservice_bot
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
BOT_TOKEN=YOUR_BOT_TOKEN
OWNER_ID=YOUR_TELEGRAM_ID
```

Run the bot:

```bash
python bot.py
```

---

## 📁 Project Structure
autoservice_bot/

│

├── bot.py
├── handlers.py
├── database.py
├── config.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md

---

## 🚀 Roadmap

### ✅ v1.0.0
- Initial release
- `/start` command
- Customer request form
- Request forwarding to the owner

### ✅ v1.1.0
- Added reply keyboard buttons
- Added request cancellation
- Added phone number validation

### ✅ v1.2.0
- Added SQLite database
- Requests are saved with date and status

---

## 📄 License

This project is licensed under the MIT License.

---

# 🇷🇺 Русский

Telegram-бот для приёма заявок на ремонт автомобилей от клиентов и автоматической отправки их владельцу сервиса.

---

## 📖 Описание

**AutoService Telegram Bot** помогает автомастерским автоматизировать процесс приёма заявок от клиентов.

---

## ✨ Возможности

- 🚀 `/start` — Приветственное сообщение
- 📝 Создать заявку через кнопку
- 👤 Сбор имени клиента
- 📞 Сбор и валидация номера телефона
- 🚗 Сбор марки и модели автомобиля
- 🔧 Сбор описания проблемы
- 📨 Отправка заявки владельцу
- ❌ Отмена заявки в любой момент
- 💾 Сохранение заявок в базу данных SQLite

---

## 🛠 Технологии

- Python
- aiogram
- aiosqlite
- python-dotenv
- aiohttp-socks

---

## 📦 Установка

```bash
git clone https://github.com/avenue54/autoservice_bot.git
cd autoservice_bot
```

```bash
pip install -r requirements.txt
```

Создай файл `.env`:

```env
BOT_TOKEN=ВАШ_ТОКЕН_БОТА
OWNER_ID=ВАШ_TELEGRAM_ID
```

```bash
python bot.py
```

---

## 📁 Структура проекта
autoservice_bot/

│
├── bot.py
├── handlers.py
├── database.py
├── config.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md

---

## 🚀 План развития

### ✅ v1.0.0
- Первый релиз
- Команда `/start`
- Форма заявки
- Пересылка заявки владельцу

### ✅ v1.1.0
- Кнопки Reply-клавиатуры
- Отмена заявки
- Валидация номера телефона

### ✅ v1.2.0
- База данных SQLite
- Заявки сохраняются с датой и статусом


---

## 📄 Лицензия

Проект распространяется под лицензией MIT.