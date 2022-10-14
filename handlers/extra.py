from aiogram import types, Dispatcher
from config import bot, ADMIN
import random


async def echo(message: types.Message):
    emoji = ['🎲', '🏀', '⚽️', '🎯', '🎳', '🎰']
    if message.text.startswith('game'):
        if message.from_user.id not in ADMIN:
            await message.answer("Доступно только для админов!")
        else:
            await bot.send_dice(message.chat.id, emoji=random.choice(emoji))
    elif message.text.isdigit():
        await bot.send_message(message.chat.id, int(message.text)*int(message.text))
    else:
        await bot.send_message(message.chat.id, message.text)


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)
