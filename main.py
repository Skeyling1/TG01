import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

bot = Bot(token='')
dp = Dispatcher()

@dp.message(CommandStart)
async def start(message: Message):
    await message.answer()


async def main():
    await dp.stop_polling()


if __name__ =='__main__':
    asyncio.run(main())