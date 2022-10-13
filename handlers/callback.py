from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot


async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton('Следующий вопрос', callback_data='button_call_2')
    markup.add(button_call_1)

    question = 'Какая из этих способностей действует сквозь защиту от магии?'
    answers = [
        'Finger Of Death',
        'Adaptive Strike',
        'Dismember',
        'Mystic Flare',
        'Shadowraze'
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=True,
        type='quiz',
        correct_option_id=2,
        open_period=60,
        reply_markup=markup
    )


async def quiz_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton('Следующий вопрос', callback_data='button_call_3')
    markup.add(button_call_1)
    question = 'Какой из этих персонажей не является иллюзионистом?'
    answers = [
        'Chaos Knight',
        'Naga Siren',
        'Phantom Lancer',
        'Meepo',
        'Terrorblade'
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=True,
        type='quiz',
        correct_option_id=3,
        open_period=60,
        reply_markup=markup
    )


async def quiz_4(call: types.CallbackQuery):
    question = 'Какой из этих предметов имеет стоимость в 5050 золотых монет?'
    answers = [
        'Black King Bar',
        'Satanic',
        'Refresher Orb',
        'Blink Dagger',
        'Boots Of Travel'
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=True,
        type='quiz',
        correct_option_id=1,
        open_period=60,
        explanation="Спасибо что прошли викторину!"
    )


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, lambda call: call.data == "button_call_1")
    dp.register_callback_query_handler(quiz_3, lambda call: call.data == "button_call_2")
    dp.register_callback_query_handler(quiz_4, lambda call: call.data == "button_call_3")
