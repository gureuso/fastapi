# -*- coding: utf-8 -*-
from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import FileResponse

from apps.common.response import PermissionDeniedException, error, NotFoundException
from config import Config

app = FastAPI()
app.mount('/static', StaticFiles(directory=Config.STATIC_DIR), name='static')

templates = Jinja2Templates(directory=Config.TEMPLATES_DIR)


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
    return {'ping': 'pong'}


@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse(f'{Config.STATIC_DIR}/favicon.ico')
