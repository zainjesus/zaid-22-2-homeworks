from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot
import random


async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id, f" Приветствую, {message.from_user.first_name}!\nДля полной информации"
                                                 f" обо мне воспользуйтесь командой /help")


async def help_handler(message: types.Message):
    await bot.send_message(message.from_user.id, 'Чтобы начать викторину, введите команду /quiz'
                                                 '\nЧтобы получить случайный мем, введите команду /meme'
                                                 '\nЧтобы сыграть со мной в кости, введите /dice'
                                                 '\nЧтобы закрепить сообщение, введите команду !pin'
                                                 ' в ответе на это сообщение'
                                                 '\nЧтобы открепить все сообщения, закрепленные мной'
                                                 ', введите команду !unpinall'
                                                 '\nЕсли начать сообщение со слова "game", то я отправлю случайный '
                                                 'анимированный эмодзи (доступно только для админов)'
                                                 '\nТакже вы можете отправить мне целое число,'
                                                 ' и я возведу его в квадрат'
                                                 '\nВ противном случае я просто повторю за вами')


async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton('Следующий вопрос', callback_data='button_call_1')
    markup.add(button_call_1)

    question = 'Какому персонажу из вселенной Dota 2 принадлежит способность Requiem Of Souls?'
    answers = [
        'Arc Warden',
        'Tinker',
        'Shadow Fiend',
        'Morphling',
        'Invoker'
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=True,
        type='quiz',
        correct_option_id=2,
        open_period=60,
        reply_markup=markup
    )


async def meme(message: types.Message):
    photo = open('media/mem1.jpg', 'rb')
    photo2 = open('media/mem2.jpg', 'rb')
    photo3 = open('media/mem3.jpg', 'rb')
    photo4 = open('media/mem4.jpg', 'rb')
    photo5 = open('media/mem5.jpg', 'rb')
    photo6 = open('media/mem6.jpg', 'rb')
    photo7 = open('media/mem7.jpg', 'rb')
    photo8 = open('media/mem8.jpg', 'rb')
    photo9 = open('media/mem9.jpg', 'rb')
    photo10 = open('media/mem10.jpg', 'rb')
    lst = [photo, photo2, photo3, photo4, photo5, photo6, photo7, photo8, photo9, photo10]
    await bot.send_photo(message.from_user.id, random.choice(lst))


async def pin(message: types.Message):
    if not message.reply_to_message:
        await message.answer("Команда должна быть ответом на сообщение!")
    else:
        await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)


async def unpin(message: types.Message):
    await bot.unpin_all_chat_messages(message.chat.id)
    await message.answer("Все сообщения были успешно откреплены!")


async def dice(message: types.Message):
    await message.answer("Бот бросает кости...")
    bot_result = await bot.send_dice(message.chat.id)
    await message.answer("Вы бросаете кости...")
    player_result = await bot.send_dice(message.chat.id)
    if bot_result.dice.value > player_result.dice.value:
        await message.answer("Бот победил!")
    elif bot_result.dice.value < player_result.dice.value:
        await message.answer("Вы победили!")
    elif bot_result.dice.value == player_result.dice.value:
        await message.answer("Ничья!")


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(help_handler, commands=['help'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(meme, commands=['mem'])
    dp.register_message_handler(pin, commands=['pin'], commands_prefix='!')
    dp.register_message_handler(unpin, commands=['unpinall'], commands_prefix='!')
    dp.register_message_handler(dice, commands=['dice'])
