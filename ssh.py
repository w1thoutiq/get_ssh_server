from asyncio import run

from aiogram import Bot, Dispatcher
from aiogram.types import Message, FSInputFile


async def func(message: Message):
    with open('/root/.shh/id_rsa.pub') as f:
        ssh = f.readline()
    await message.answer(
        text=f'<code>{ssh}</code>',
        parse_mode='html'
    )


async def start():
    bot = Bot(token='6073317405:AAERVk7dxQIKDZ4VU42s_w4Va2Zgaq5a8S0')
    dp = Dispatcher()
    dp.message.register(func)

    await dp.start_polling(bot)

run(start())
