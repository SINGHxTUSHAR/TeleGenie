"""
@Author: TUSHAR SINGH
@Topic: ChatBot // TeleGenie
@GitHub: https://github.com/SINGHxTUSHAR/TeleGenie
@reference: OpenAI , Aiogram, BotFather
"""

import logging
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os

load_dotenv()
API_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

#configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def command_start_handler(message: types.Message):
    """
    This handler receives messages with `/start` or  `/help `command
    """
    await message.reply("Hi\nI am TeleGenie Bot!\nPowered by aiogram.")
    
    
@dp.message_handler()
async def echo(message: types.Message):
    """
    This will retrun echo
    """
    await message.answer(message.text)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)





