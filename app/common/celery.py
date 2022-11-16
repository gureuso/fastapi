from celery import Celery

from config import Config

app = Celery('celery', backend=f'redis://{Config.REDIS_HOST}', broker=f'redis://{Config.REDIS_HOST}')


@app.task
def celery_hello_world() -> str:
    return 'hello world!!!'
