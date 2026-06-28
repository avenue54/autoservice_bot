import aiosqlite
from datetime import datetime

DB_PATH = 'database.db'

async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await  db.execute('''
            CREATE TABLE IF NOT EXISTS requests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            phone TEXT,
            brand TEXT,
            problem TEXT,
            date TEXT,
            status TEXT DEFAULT 'active'
            )
            ''')
        
        await db.commit()
        
        
async def save_request(name, phone, brand, problem):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute('''
            INSERT INTO requests (name, phone, brand, problem, date, status) 
            VALUES (?, ?, ?, ?, ?, 'active')
            ''', (name, phone, brand, problem, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        await db.commit()