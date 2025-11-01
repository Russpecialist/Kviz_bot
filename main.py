import asyncio
from aiogram import types, F
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from config import bot, dp
from database import create_table, get_quiz_index, update_quiz_index, get_user_score, update_user_score
from logic import  generate_options_keyboard
from data import quiz_data
from logic import get_question, new_quiz
# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text="Начать игру"))
    await message.answer("Добро пожаловать в квиз!", reply_markup=builder.as_markup(resize_keyboard=True))



@dp.message(F.text == "Начать игру")
@dp.message(Command("quiz"))
async def cmd_quiz(message: types.Message):
    await message.answer("Давайте начнем квиз!")
    await new_quiz(message)

@dp.message(Command("help"))
async def cmd_help(message:types.Message):
    await message.answer("Команды бота:\n/start - Начать взаимодействие с ботом\n/help - открыть помощь\n/quiz - начать игру")

async def main():
    await create_table()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())