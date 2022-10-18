from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


direction_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
)

gender_a = KeyboardButton('Backend')
gender_b = KeyboardButton('Fronted')
gender_c = KeyboardButton('Android')
gender_d = KeyboardButton('IOS')
gender_e = KeyboardButton('UX/UI')


direction_markup.add(gender_a, gender_b, gender_c, gender_d, gender_e).add(KeyboardButton('CANCEL'))


submit_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(KeyboardButton('ДА'), KeyboardButton('НЕТ'))

cancel_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(KeyboardButton('CANCEL'))
