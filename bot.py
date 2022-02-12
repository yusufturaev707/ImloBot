import logging, api, check_words
from transliterate import to_cyrillic, to_latin

from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=api.API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await message.reply(f"Assalomu aleykum {message.chat.username}. "
                        f"\nImlo botiga xush kelibsiz.")


@dp.message_handler(commands=['help'])
async def command_help(message: types.Message):
    await message.reply(f"Botdan foydalanish uchun so'z yuboring.")


@dp.message_handler()
async def checkImlo(message: types.Message):
    word = message.text
    words = word.split()
    for word in words:
        is_latin = False
        for item in word.lower():
            if 96 < ord(item) < 123:
                is_latin = True
        if is_latin:
            word = to_cyrillic(word.lower())
        result = check_words.checkWord(word)
        if is_latin:
            word = to_latin(word.capitalize())
        if result['available']:
            response = f"✅ {word.capitalize()}"
        else:
            response = f"❌ {word.capitalize()}"
            for text in result['matches']:
                if is_latin:
                    text = to_latin(text)
                response += f"\n✅ {text.capitalize()}"
        await message.answer(response)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
