import os
import logging
import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.exceptions import TelegramAPIError
from translit import transliterate

logging.basicConfig(
    filename="bot.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise RuntimeError("BOT_TOKEN не найден")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command(commands=["start"]))
async def start_handler(message: types.Message):
    await message.answer(
        "Отправьте ФИО на кириллице, я сделаю транслитерацию.\n\n"
        "Если нужна помощь — напишите /help."
    )

@dp.message(Command(commands=["help"]))
async def help_handler(message: types.Message):
    await message.answer(
        "Отправь ФИО на кириллице (например, Иванов Иван Иванович), "
        "я верну транслитерацию по приказу МИД.\n"
        "Поддерживаются только буквы и пробелы."
    )

@dp.message()
async def translit_handler(message: types.Message):
    text = message.text.strip()
    logging.info(f"Получено сообщение от {message.from_user.id}: {text}")

    if not all(ch.isalpha() or ch.isspace() for ch in text):
        await message.answer("Пожалуйста, введите только буквы и пробелы.")
        return

    words = text.split()
    if len(words) < 2:
        await message.answer("Пожалуйста, введите как минимум фамилию и имя.")
        return

    try:
        latin = transliterate(text)
    except Exception as e:
        logging.error(f"Ошибка при транслитерации: {e}")
        await message.answer("Произошла ошибка, попробуйте ещё раз.")
        return

    logging.info(f"Отправляю ответ пользователю {message.from_user.id}: {latin}")
    await message.answer(latin)

async def main():
    try:
        await dp.start_polling(bot)
    except TelegramAPIError as e:
        logging.error(f"Ошибка Telegram API: {e}")

if __name__ == "__main__":
    asyncio.run(main())
