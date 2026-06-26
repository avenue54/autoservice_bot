# config.py
import os
from dotenv import load_dotenv

# Читаем переменные из файла .env и загружаем в окружение
load_dotenv()

# Получаем значения из окружения
BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID"))  # int() — потому что ID это число