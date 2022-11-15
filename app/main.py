# -*- coding: utf-8 -*-
from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import FileResponse
from starlette.exceptions import HTTPException

from app.common.response import PermissionDeniedException, error, NotFoundException
from app.database.sqlite import database
from app.common.cron import scheduler
from app.router.v1.user.router import router as v1_user_router
from config import Config

app = FastAPI(docs_url='/H9buCGuR', redoc_url='/Ff9Wbe2S', openapi_url='/vOWksi3t')
app.include_router(v1_user_router)
app.mount('/static', StaticFiles(directory=Config.STATIC_DIR), name='static')

templates = Jinja2Templates(directory=Config.TEMPLATES_DIR)


@app.exception_handler(HTTPException)
async def not_found_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(status_code=exc.status_code, content=error(exc.status_code * 100))


@app.exception_handler(PermissionDeniedException)
async def permission_denied_exception_handler(request: Request, exc: PermissionDeniedException):
    return JSONResponse(status_code=403, content=error(40300))


@app.exception_handler(NotFoundException)
async def not_found_exception_handler(request: Request, exc: NotFoundException):
    return JSONResponse(status_code=404, content=error(40400))


@app.exception_handler(Exception)
async def exception_handler(request: Request, exc: Exception):
    print(exc)
    return JSONResponse(status_code=500, content=error(50000))


@app.get('/')
@app.get('/ping')
async def ping():
    # await Kafka.producer.send('fastapi_topic', json.dumps({'username': 'alex'}).encode('utf-8'))
    return {'ping': 'pong'}


@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse(f'{Config.STATIC_DIR}/favicon.ico')


@app.on_event('startup')
async def startup():
    scheduler.start()
    await database.connect()
    # kafka = Kafka()
    # await kafka.start()


@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()
    # await Kafka.producer.stop()
