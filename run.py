import uvicorn

from config import Config

if __name__ == '__main__':
    uvicorn.run(
        'app.main:app',
        host=Config.APP_HOST,
        port=Config.APP_PORT,
        reload=not Config.is_production(),
        workers=4,
        log_level='info' if not Config.is_production() else 'warning',
    )
