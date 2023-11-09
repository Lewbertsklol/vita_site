import os

from aiogram import Bot
from aiogram.client.session.aiohttp import AiohttpSession


TOKEN = os.environ['BOT_TOKEN']


def create_message(
        client_firstname: str,
        client_lastname,
        client_phone: str,
        month: str,
        day: str,
        time: str):
    return f"Записался клиент:\n" \
        f"{month} - {day} число - {time}\n" \
        f"{client_firstname} {client_lastname}\n" \
        f"{client_phone}"


async def bot_notification(
    client_firstname: str,
    client_lastname,
    client_phone: str,
    month: str,
    day: str,
    time: str
) -> None:
    session = AiohttpSession()
    bot = Bot(TOKEN, session=session)
    message = create_message(
        client_firstname, client_lastname, client_phone, month, day, time)
    await bot.send_message(915877828, message)
    await bot.send_message(5833095324, message)
    await session.close()
