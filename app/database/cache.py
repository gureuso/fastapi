from redis import asyncio as aioredis

from config import Config

cache = aioredis.from_url(f'redis://{Config.REDIS_HOST}')


class Cache:
    @staticmethod
    async def keys(pattern: str = '*'):
        return await cache.keys(pattern)


    @staticmethod
    async def get(key: str):
        return await cache.get(key)

    @staticmethod
    async def set(key: str, value: str):
        return await cache.set(key, value)
