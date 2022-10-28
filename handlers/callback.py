from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot
from database.bot_db import sql_command_delete
from parser_rezkahd.movies import get_horror, get_fiction, get_action, get_detective
from parser_rezkahd.movies import get_horror_serial, get_fantasy, get_action_serial, get_detective_serial
from parser_rezkahd.movies import get_senen, get_mystery, get_drama, get_detective_anime
from parser_rezkahd.movies import get_fairy, get_fiction_cartoon, get_comedy, get_soviet


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
        chat_id=call.message.chat.id,
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
        chat_id=call.message.chat.id,
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
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=True,
        type='quiz',
        correct_option_id=1,
        open_period=60,
        explanation="Спасибо что прошли викторину!"
    )


async def complete_delete(call: types.CallbackQuery):
    await sql_command_delete(call.data.replace('delete ', ''))
    await call.answer(text="Ментор удален из базы данных", show_alert=True)
    await bot.delete_message(call.message.chat.id, call.message.message_id)


async def film_genre(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    horror = InlineKeyboardButton('Ужасы', callback_data="button_horror_film")
    fiction = InlineKeyboardButton('Фантастика', callback_data="button_fiction_film")
    action = InlineKeyboardButton('Боевики', callback_data="button_action_film")
    detective = InlineKeyboardButton('Детектив', callback_data="button_detective_film")
    markup.add(horror, fiction, action, detective)
    await bot.send_message(call.from_user.id, 'Выберите жанр фильма', reply_markup=markup)


async def serial_genre(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    horror = InlineKeyboardButton('Ужасы', callback_data="button_horror_serial")
    fiction = InlineKeyboardButton('Фэнтези', callback_data="button_fantasy_serial")
    action = InlineKeyboardButton('Боевики', callback_data="button_action_serial")
    detective = InlineKeyboardButton('Детектив', callback_data="button_detective_serial")
    markup.add(horror, fiction, action, detective)
    await bot.send_message(call.from_user.id, 'Выберите жанр сериала', reply_markup=markup)


async def anime_genre(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    senen = InlineKeyboardButton('Сёнэн', callback_data="button_senen")
    mystery = InlineKeyboardButton('Мистика', callback_data="button_mystery")
    drama = InlineKeyboardButton('Драмы', callback_data="button_drama")
    detective = InlineKeyboardButton('Детектив', callback_data="button_detective_anime")
    markup.add(senen, mystery, drama, detective)
    await bot.send_message(call.from_user.id, 'Выберите жанр аниме', reply_markup=markup)


async def cartoon_genre(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    fairy = InlineKeyboardButton('Сказки', callback_data="button_fairy")
    fiction = InlineKeyboardButton('Фантастика', callback_data="button_fiction_cartoon")
    comedy = InlineKeyboardButton('Комедии', callback_data="button_comedy")
    soviet = InlineKeyboardButton('Советские', callback_data="button_soviet")
    markup.add(fairy, fiction, comedy, soviet)
    await bot.send_message(call.from_user.id, 'Выберите жанр мультфильма', reply_markup=markup)


async def parser_horror(call: types.callback_query):
    items = get_horror()
    for item in items:
        await bot.send_message(call.from_user.id,
                               f"{item['link']}\n\n"
                               f"{item['title']}\n"
                               f"{item['length']}\n"
                               f"{item['year']}\n"
                               f"{item['country']}\n"
                               )


async def parser_fiction(call: types.callback_query):
    items = get_fiction()
    for item in items:
        await bot.send_message(call.from_user.id,
                               f"{item['link']}\n\n"
                               f"{item['title']}\n"
                               f"{item['length']}\n"
                               f"{item['year']}\n"
                               f"{item['country']}\n"
                               )


async def parser_action(call: types.callback_query):
    items = get_action()
    for item in items:
        await bot.send_message(call.from_user.id,
                               f"{item['link']}\n\n"
                               f"{item['title']}\n"
                               f"{item['length']}\n"
                               f"{item['year']}\n"
                               f"{item['country']}\n"
                               )


async def parser_detective(call: types.callback_query):
    items = get_detective()
    for item in items:
        await bot.send_message(call.from_user.id,
                               f"{item['link']}\n\n"
                               f"{item['title']}\n"
                               f"{item['length']}\n"
                               f"{item['year']}\n"
                               f"{item['country']}\n"
                               )


async def parser_horror_serial(call: types.callback_query):
    items = get_horror_serial()
    for item in items:
        await bot.send_message(call.from_user.id,
                               f"{item['link']}\n\n"
                               f"{item['title']}\n"
                               f"{item['length']}\n"
                               f"{item['year']}\n"
                               f"{item['country']}\n"
                               )


async def parser_fantasy(call: types.callback_query):
    items = get_fantasy()
    for item in items:
        await bot.send_message(call.from_user.id,
                               f"{item['link']}\n\n"
                               f"{item['title']}\n"
                               f"{item['length']}\n"
                               f"{item['year']}\n"
                               f"{item['country']}\n"
                               )


async def parser_action_serial(call: types.callback_query):
    items = get_action_serial()
    for item in items:
        await bot.send_message(call.from_user.id,
                               f"{item['link']}\n\n"
                               f"{item['title']}\n"
                               f"{item['length']}\n"
                               f"{item['year']}\n"
                               f"{item['country']}\n"
                               )


async def parser_detective_serial(call: types.callback_query):
    items = get_detective_serial()
    for item in items:
        await bot.send_message(call.from_user.id,
                               f"{item['link']}\n\n"
                               f"{item['title']}\n"
                               f"{item['length']}\n"
                               f"{item['year']}\n"
                               f"{item['country']}\n"
                               )


async def parser_senen(call: types.callback_query):
    items = get_senen()
    for item in items:
        await bot.send_message(call.from_user.id,
                               f"{item['link']}\n\n"
                               f"{item['title']}\n"
                               f"{item['length']}\n"
                               f"{item['year']}\n"
                               f"{item['country']}\n"
                               )


async def parser_mystery(call: types.callback_query):
    items = get_mystery()
    for item in items:
        await bot.send_message(call.from_user.id,
                               f"{item['link']}\n\n"
                               f"{item['title']}\n"
                               f"{item['length']}\n"
                               f"{item['year']}\n"
                               f"{item['country']}\n"
                               )


async def parser_drama(call: types.callback_query):
    items = get_drama()
    for item in items:
        await bot.send_message(call.from_user.id,
                               f"{item['link']}\n\n"
                               f"{item['title']}\n"
                               f"{item['length']}\n"
                               f"{item['year']}\n"
                               f"{item['country']}\n"
                               )


async def parser_detective_anime(call: types.callback_query):
    items = get_detective_anime()
    for item in items:
        await bot.send_message(call.from_user.id,
                               f"{item['link']}\n\n"
                               f"{item['title']}\n"
                               f"{item['length']}\n"
                               f"{item['year']}\n"
                               f"{item['country']}\n"
                               )


async def parser_fairy(call: types.callback_query):
    items = get_fairy()
    for item in items:
        await bot.send_message(call.from_user.id,
                               f"{item['link']}\n\n"
                               f"{item['title']}\n"
                               f"{item['length']}\n"
                               f"{item['year']}\n"
                               f"{item['country']}\n"
                               )


async def parser_fiction_cartoon(call: types.callback_query):
    items = get_fiction_cartoon()
    for item in items:
        await bot.send_message(call.from_user.id,
                               f"{item['link']}\n\n"
                               f"{item['title']}\n"
                               f"{item['length']}\n"
                               f"{item['year']}\n"
                               f"{item['country']}\n"
                               )


async def parser_comedy(call: types.callback_query):
    items = get_comedy()
    for item in items:
        await bot.send_message(call.from_user.id,
                               f"{item['link']}\n\n"
                               f"{item['title']}\n"
                               f"{item['length']}\n"
                               f"{item['year']}\n"
                               f"{item['country']}\n"
                               )


async def parser_soviet(call: types.callback_query):
    items = get_soviet()
    for item in items:
        await bot.send_message(call.from_user.id,
                               f"{item['link']}\n\n"
                               f"{item['title']}\n"
                               f"{item['length']}\n"
                               f"{item['year']}\n"
                               f"{item['country']}\n"
                               )


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, lambda call: call.data == "button_call_1")
    dp.register_callback_query_handler(quiz_3, lambda call: call.data == "button_call_2")
    dp.register_callback_query_handler(quiz_4, lambda call: call.data == "button_call_3")
    dp.register_callback_query_handler(complete_delete,
                                       lambda call: call.data and call.data.startswith('delete '))

    dp.register_callback_query_handler(film_genre, lambda call: call.data == "button_film")
    dp.register_callback_query_handler(serial_genre, lambda call: call.data == "button_serial")
    dp.register_callback_query_handler(anime_genre, lambda call: call.data == "button_anime")
    dp.register_callback_query_handler(cartoon_genre, lambda call: call.data == "button_cartoon")

    dp.register_callback_query_handler(parser_horror, lambda call: call.data == "button_horror_film")
    dp.register_callback_query_handler(parser_fiction, lambda call: call.data == "button_fiction_film")
    dp.register_callback_query_handler(parser_action, lambda call: call.data == "button_action_film")
    dp.register_callback_query_handler(parser_detective, lambda call: call.data == "button_detective_film")

    dp.register_callback_query_handler(parser_horror_serial, lambda call: call.data == "button_horror_serial")
    dp.register_callback_query_handler(parser_fantasy, lambda call: call.data == "button_fantasy_serial")
    dp.register_callback_query_handler(parser_action_serial, lambda call: call.data == "button_action_serial")
    dp.register_callback_query_handler(parser_detective_serial, lambda call: call.data == "button_detective_serial")

    dp.register_callback_query_handler(parser_senen, lambda call: call.data == "button_senen")
    dp.register_callback_query_handler(parser_mystery, lambda call: call.data == "button_mystery")
    dp.register_callback_query_handler(parser_drama, lambda call: call.data == "button_drama")
    dp.register_callback_query_handler(parser_detective_anime, lambda call: call.data == "button_detective_anime")

    dp.register_callback_query_handler(parser_fairy, lambda call: call.data == "button_fairy")
    dp.register_callback_query_handler(parser_fiction_cartoon, lambda call: call.data == "button_fiction_cartoon")
    dp.register_callback_query_handler(parser_comedy, lambda call: call.data == "button_comedy")
    dp.register_callback_query_handler(parser_soviet, lambda call: call.data == "button_soviet")
