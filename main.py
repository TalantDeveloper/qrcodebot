from aiogram import Bot, Dispatcher, executor, types
import pyqrcode
import png

BOT_TOKEN = "1705700560:AAEFaay7JIkSfrKOL5BmGGZJIfTOZvMgs1U"
bot = Bot(token=BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    await bot.send_message(556841744, f"<b>User : {message.from_user.full_name}</b>\n"
                                      f"ID : {message.from_user.id}")

    await message.reply(f"Hello. \n This is bot QR code bot.")


@dp.message_handler(commands=['bot_developer', 'admin'])
async def developer(message: types.Message):
    text = f"Hello! My name is Botirjon. \nI am a student. " \
           f"I like study. \nI can do web backend and telegram bot. " \
           f"Contact phone: +998995907850.\n" \
           f"GitHub profile: https://github.com/TalandBotirjon"
    await bot.send_message(556841744, f"User : {message.from_user.full_name}\n"
                                      f"ID : {message.from_user.id}")
    await message.reply(text)


@dp.message_handler()
async def qr(message: types.Message):
    text = pyqrcode.create(message.text)
    text.png('code.png', scale=8)
    await bot.send_message(556841744, f"User : {message.from_user.full_name}\n"
                                      f"ID : {message.from_user.id}")

    await bot.send_photo(chat_id=message.chat.id, photo=open('code.png', 'rb'))


executor.start_polling(dp)
