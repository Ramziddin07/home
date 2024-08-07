import logging
from transliterate import to_latin, to_cyrillic
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '7295794084:AAE9NLw6tHtb3dCutuSS3arPuFTVRCCVXm8'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends /start or /help command
    """
    await message.reply("Salom\nKrill lotin botimizga xush kelibsiz\nMatiningizni kiriting.")



@dp.message_handler()
async def echo(message: types.Message):
    msg = message.text
    javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)

    await message.answer(javob(msg))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)