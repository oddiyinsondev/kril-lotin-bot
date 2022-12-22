import logging
from aiogram import Dispatcher, Bot, executor, types
from kril_lotin import to_cyrillic, to_latin
from bot import TOKKEN

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start",])
async def boshlash(message: types.Message):
    odi = message.from_user.first_name
    await message.answer(f"Assalom-u alaykum {odi}\nSizga kril-lotin lotin-krilga o'tgazadigan botman")


@dp.message_handler()
async def latin(message: types.Message):
    text = message.text

    if text.isascii():
        kril = to_cyrillic(text)
        await message.reply(kril)
    else:
        lotincha = to_latin(text)
        await message.reply(lotincha)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
