from redis import asyncio as aioredis

from config import Config

redis = aioredis.from_url(f'redis://{Config.REDIS_HOST}')


class Redis:
    @staticmethod
    async def get(key: str):
        return await redis.get(key)
