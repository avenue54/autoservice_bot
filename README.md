git tag# 🚗 AutoService Telegram Bot


<p align="center">
  <a href="#-english">🇬🇧 English</a> •
  <a href="#-русский">🇷🇺 Русский</a>
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
- 📝 `/request` — Create a new repair request
- 👤 Collect customer's name
- 📞 Collect phone number
- 🚗 Collect car make and model
- 🔧 Collect problem description
- 📨 Send the completed request to the owner
- ❌ Cancel request at any time
- ✅ Phone number validation

---

## 💬 Example

### Customer

```
/request
```

```
Name: Daniel
Phone: +79001234567
Car: Lada Vesta
Problem: Engine won't start
```

### Owner receives

```
📋 New Request

👤 Name: Daniel
📞 Phone: +79001234567
🚗 Car: Lada Vesta
🔧 Problem: Engine won't start
```

---

## 🛠 Technologies

- Python
- aiogram
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

```
autoservice_bot/
│
├── bot.py
├── handlers/
├── keyboards/
├── .env
├── requirements.txt
└── README.md
```

---

## 🚀 Roadmap

### ✅ v1.0.0

- Initial release
- `/start` command
- `/request` command
- Customer request form
- Request forwarding to the owner

### ✅ v1.1.0

- Added request cancellation
- Added phone number validation

### 🔜 Planned Features

- Reply keyboard buttons
- SQLite database
- Request history
- Admin panel
- Service categories
- Working hours
- FAQ with AI support

---

## 🤝 Contributing

Pull requests and suggestions are welcome.

---
## 📄 License

This project is licensed under the MIT License.



# 🇷🇺 Русский

## Описание

# 🚗 Бот для автосервиса

Telegram-бот для приёма заявок на ремонт автомобилей от клиентов и автоматической отправки их владельцу сервиса.

---

## 📖 Описание

**AutoService Telegram Bot** помогает автомастерским автоматизировать процесс приёма заявок от клиентов.

Бот собирает всю необходимую информацию от клиента и мгновенно отправляет оформленную заявку владельцу сервиса.

---

## ✨ Возможности

- 🚀 `/start` — Приветственное сообщение
- 📝 `/request` — Создать новую заявку на ремонт
- 👤 Сбор имени клиента
- 📞 Сбор номера телефона
- 🚗 Сбор марки и модели автомобиля
- 🔧 Сбор описания проблемы
- 📨 Отправка готовой заявки владельцу
- ❌ Отмена заявки в любой момент
- ✅ Валидация номера телефона

---

## 💬 Пример

### Клиент

```
/request
```
Имя: Даниил

Телефон: +79001234567

Автомобиль: Lada Vesta

Проблема: Двигатель не заводится

### Владелец получает
📋 Новая заявка
👤 Имя: Даниил

📞 Телефон: +79001234567

🚗 Автомобиль: Lada Vesta

🔧 Проблема: Двигатель не заводится

---

## 🛠 Технологии

- Python
- aiogram
- python-dotenv
- aiohttp-socks

---

## 📦 Установка

Клонируй репозиторий:

```bash
git clone https://github.com/avenue54/autoservice_bot.git
cd autoservice_bot
```

Установи зависимости:

```bash
pip install -r requirements.txt
```

Создай файл `.env`:

```env
BOT_TOKEN=ВАШ_ТОКЕН_БОТА
OWNER_ID=ВАШ_TELEGRAM_ID
```

Запусти бота:

```bash
python bot.py
```

---

## 📁 Структура проекта
autoservice_bot/

│

├── bot.py

├── handlers/

├── keyboards/

├── .env

├── requirements.txt

└── README.md

---

## 🚀 План развития

### ✅ v1.0.0

- Первый релиз
- Команда `/start`
- Команда `/request`
- Форма заявки от клиента
- Пересылка заявки владельцу

### ✅ v1.1.0

- Добавлена отмена заявки
- Добавлена валидация номера телефона

### 🔜 Планируется

- Кнопки Reply-клавиатуры
- База данных SQLite
- История заявок
- Админ-панель
- Категории услуг
- Часы работы
- FAQ с поддержкой ИИ

---

## 🤝 Вклад в проект

Pull request'ы и предложения приветствуются.

---

## 📄 Лицензия

Проект распространяется под лицензией MIT.