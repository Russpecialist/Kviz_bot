
import logging
from aiogram import Bot, Dispatcher
import os
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)
load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")


def check_env_file():
    """Проверяет наличие и читаемость .env файла"""
    env_path = '.env'
    
    # Проверяем существование файла
    if not os.path.exists(env_path):
        print(f"❌ Файл {env_path} не найден!")
        print("Создайте файл .env в той же папке что и main.py")
        return False
    
    # Проверяем, что это файл, а не папка
    if not os.path.isfile(env_path):
        print(f"❌ {env_path} это не файл!")
        return False
    
    # Проверяем размер файла
    if os.path.getsize(env_path) == 0:
        print(f"❌ Файл {env_path} пустой!")
        return False
    
    print(f"✅ Файл {env_path} найден")
    return True

# Проверяем файл перед загрузкой
if not check_env_file():
    exit(1)
# Объект бота
bot = Bot (token =API_TOKEN)
dp = Dispatcher()


# Имя базы данных
DB_NAME = 'quiz_bot.db'

