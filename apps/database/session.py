import os
import aiosqlite
import functools

from config import Config


def connect():
    def wrapper(func):
        @functools.wraps(func)
        async def wrapped(*args, **kwargs):
            db = await aiosqlite.connect(os.path.join(Config.ROOT_DIR, 'fastapi.db'))
            res = await func(*args, db, **kwargs)
            await db.close()
            return res
        return wrapped
    return wrapper


class SQLITE:
    @staticmethod
    @connect()
    async def find(query: str, db):
        cursor = await db.execute(query)
        res = await cursor.fetchall()
        await cursor.close()
        return res

    @staticmethod
    @connect()
    async def find_one(query: str, db):
        cursor = await db.execute(query)
        res = await cursor.fetchone()
        await cursor.close()
        return res

    @staticmethod
    @connect()
    async def execute(query: str, db):
        cursor = await db.execute(query)
        await cursor.close()

    @staticmethod
    @connect()
    async def init(db):
        cursor = await db.execute('''
            CREATE TABLE user (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email VARCHAR(255) NOT NULL UNIQUE
            );
        ''')
        await cursor.close()
