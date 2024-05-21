from fastapi import FastAPI, Request
import uvicorn

from aiogram import types

class Config:
    TOKEN = '6602011107:AAH1E4TjYFCMr3P9V1oXFR6ZCkuKPDawJDs'
    WEBHOOK_HOST = 'https://45.15.158.189'
    WEBHOOK_PATH = '/webhook'
    WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"
    WEBAPP_HOST = '0.0.0.0'
    WEBAPP_PORT = 8000
    TELEGRAM_SECRET_TOKEN = 'YOUR_SECRET_TOKEN'  # Секретный токен для проверки

cfg = Config()

app = FastAPI()

@app.post(cfg.WEBHOOK_PATH)
async def bot_webhook(request: Request):
    try:
        update = types.Update(**await request.json())
        # Обработка данных вебхука
        return {"status": "ok"}
    except Exception as e:
        return {"status": "error"}

if __name__ == "__main__":
    uvicorn.run(app, host=cfg.WEBAPP_HOST, port=cfg.WEBAPP_PORT)
