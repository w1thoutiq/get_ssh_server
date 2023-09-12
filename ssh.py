from asyncio import run

from aiogram import Bot, Dispatcher
from aiogram.types import Message, InputFile
import logging


async def func(message: Message):
    await message.answer_document(
        document=InputFile('/root/.shh/id_rsa.pub')
    )


async def start():
    bot = Bot(token='6073317405:AAERVk7dxQIKDZ4VU42s_w4Va2Zgaq5a8S0')
    dp = Dispatcher()
    logging.basiConfig(logging.INFO)
    dp.message.register(func)

    dp.start_pooling(bot)

run(start())
