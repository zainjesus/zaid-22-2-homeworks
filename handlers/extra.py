from aiogram import types, Dispatcher
from config import bot, ADMIN
import random

emoji = ['🎲', '🏀', '⚽️', '🎯', '🎳', '🎰']


async def echo(message: types.Message):
    if message.text.startswith('game'):
        if not message.from_user.id in ADMIN:
            await message.answer("Доступно только для админа!")
        else:
            await bot.send_dice(message.chat.id, emoji=random.choice(emoji))
    elif message.text.isdigit():
        await bot.send_message(message.from_user.id, int(message.text)*int(message.text))
    else:
        await bot.send_message(message.from_user.id, message.text)


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)
