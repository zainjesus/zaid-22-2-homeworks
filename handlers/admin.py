from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, ADMIN
from database.bot_db import sql_command_all


async def delete_data(message: types.Message):
    if message.from_user.id not in ADMIN:
        await message.answer("Доступно только для админа!")
    else:
        users = await sql_command_all()
        for user in users:
            await bot.send_message(message.from_user.id,
                                   f"id ментора - {user[0]} \nИмя ментора - {user[1]}"
                                   f" \nНаправление ментора - {user[2]}"
                                   f" \nВозраст ментора - {user[3]} \nГруппа ментора - "
                                   f"{user[4]}",
                                   reply_markup=InlineKeyboardMarkup().add(
                                       InlineKeyboardButton(f"Delete {user[1]}",
                                                            callback_data=f"delete {user[0]}")
                                   ))


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(delete_data, commands=['del'])

