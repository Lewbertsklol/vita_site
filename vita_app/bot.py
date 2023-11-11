import os

from aiogram import Bot
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.enums.parse_mode import ParseMode
from aiogram.utils.formatting import PhoneNumber


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
        f'{client_phone.replace("(","").replace(")","").replace(" ", "").replace("-","")}'


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
    await bot.send_message(915877828, message, parse_mode=ParseMode.HTML)
    # await bot.send_message(5833095324, message)  #! для Виолетты
    await session.close()
