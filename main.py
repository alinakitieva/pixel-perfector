import asyncio
import logging

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command

from config_data.config import load_config
from process_image import process_image

config = load_config('config_data/.env')
bot_token = config.tg_bot.token

logging.basicConfig(level=logging.INFO)

bot = Bot(token=bot_token)
dp = Dispatcher()


# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Welcome! Send me an image and I'll enhance its quality.")


@dp.message(Command('help'))
async def cmd_help(message: types.Message):
    await message.answer("Send an image and I will improve its resolution using a Real-ESRGAN.")


@dp.message(F.text)
async def send_echo(message: types.Message):
    await message.answer(text=message.text)


@dp.message(F.photo)
async def update_photo(message: types.Message, bot: Bot):
    result_path = f"/tmp/{message.photo[-1].file_id}.jpg"
    await bot.download(
        message.photo[-1],
        destination=result_path
    )
    try:
        sr_image_path = process_image(result_path)
        with open(sr_image_path, 'rb') as img:
            await message.answer_photo(
                types.BufferedInputFile(
                    img.read(),
                    filename="buffer.jpg"
                )
            )

    except Exception as e:
        print(e)


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
