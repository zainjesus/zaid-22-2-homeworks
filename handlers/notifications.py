import aioschedule
from aiogram import types, Dispatcher
from config import bot
import asyncio


async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = message.from_user.id
    await message.answer("Ok")


async def reminder_tuesday():
    await bot.send_message(chat_id=chat_id, text='У тебя завтра урок в 20:00, не забудь!')


async def reminder_wednesday():
    await bot.send_message(chat_id=chat_id, text='Урок начинается через час!')


async def reminder_friday():
    await bot.send_message(chat_id=chat_id, text='У тебя завтра урок в 20:00, не забудь!')


async def reminder_saturday():
    await bot.send_message(chat_id=chat_id, text='Урок начинается через час!')


async def scheduler():
    aioschedule.every().tuesday.at('10:00').do(reminder_tuesday)
    aioschedule.every().wednesday.at('19:00').do(reminder_wednesday)
    aioschedule.every().friday.at('10:00').do(reminder_friday)
    aioschedule.every().sunday.at('19:00').do(reminder_saturday)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)


def register_handlers_notification(dp: Dispatcher):
    dp.register_message_handler(get_chat_id,
                                lambda word: 'Напомни' in word.text)
