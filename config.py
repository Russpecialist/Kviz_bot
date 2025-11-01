# import logging
# from aiogram import Bot, Dispatcher
# import json
# logging.basicConfig(level=logging.INFO)

# API_TOKEN = '8005117368:AAHKsYk6oeEref6nIZCCJSjn1rJ5eYqzja4'

# # Объект бота
# bot = Bot(token=API_TOKEN)
# dp = Dispatcher()

# #файл вопросов

# DICT_DATA = 'data/quiz_data.json'


# # Имя базы данных
# DB_NAME = 'quiz_bot.db'

# with open(DICT_DATA, 'r') as j:
#     quiz_data = json.loads(j.read())
import logging
from aiogram import Bot, Dispatcher
import os

logging.basicConfig(level=logging.INFO)

API_TOKEN = '8005117368:AAHKsYk6oeEref6nIZCCJSjn1rJ5eYqzja4'

# Объект бота
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


# Имя базы данных
DB_NAME = 'quiz_bot.db'

