from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import bot, ADMIN
from keyboard.client_kb import direction_markup, submit_markup, cancel_markup
import random


class FSMAdmin(StatesGroup):
    name = State()
    direction = State()
    age = State()
    group = State()
    submit = State()


async def fsm_start(message: types.Message):
    if message.chat.type == 'private':
        if message.from_user.id not in ADMIN:
            await message.answer("Эта команда доступна только для админов!")
        else:
            await message.answer(f"Привет, {message.from_user.full_name}!"
                                 f"\nУкажите имя ментора", reply_markup=cancel_markup)
            await FSMAdmin.name.set()
    else:
        await message.answer("Данная команда работает только приватной переписке с ботом!")


async def input_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        lst = []
        k = random.randint(100000, 999999)
        while k in lst:
            k = random.randint(100000, 999999)
        lst.append(k)
        data['id'] = k
        if message.text.isalpha():
            data['name'] = message.text
            await message.answer(f"Укажите направление ментора {data['name']}", reply_markup=direction_markup)
            await FSMAdmin.next()
        else:
            await message.answer("В имени не должно быть цифр и символов!")


async def input_direction(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        directions = ['backend', 'fronted', 'android', 'ios', 'ux/ui']
        if message.text.lower() in directions:
            data['direction'] = message.text
            await FSMAdmin.next()
            await message.answer(f"Укажите возраст ментора {data['name']}", reply_markup=cancel_markup)
        else:
            await message.answer("Нет такого направления!")


async def input_age(message: types.Message, state: FSMContext):
    try:
        if int(message.text) < 10 or int(message.text) > 50:
            await message.answer("Не уверен что есть ментор с таким возрастом, попробуйте еще раз")
        else:
            async with state.proxy() as data:
                data['age'] = int(message.text)
                await FSMAdmin.next()
                await message.answer(f"Укажите группу ментора {data['name']}")
    except:
        await message.answer("Нельзя использовать буквы и другие символы!")


async def input_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        flag = 0
        for i in message.text:
            if i.isalpha():
                await message.answer("В номере группы не может быть букв!")
                flag = 1
                break
        if not flag:
            data['group'] = message.text
            await bot.send_message(message.from_user.id, f"id ментора - {data['id']} \nИмя ментора - {data['name']}"
                                                         f" \nНаправление ментора - {data['direction']}"
                                                         f" \nВозраст ментора - {data['age']} \nГруппа ментора - "
                                                         f"{data['group']}")
            await FSMAdmin.next()
            await message.answer(f"Зарегистрировать ментора {data['name']}?", reply_markup=submit_markup)


async def submit(message: types.Message, state: FSMContext):
    if message.text.lower() == "да":
        await state.finish()
        await message.answer("Регистрация завершена")
    elif message.text.lower() == "нет":
        await state.finish()
        await message.answer("Регистрация отменена!")


async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer("Регистрация отменена!")


def register_handlers_fsm_admin(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, state='*', commands=['cancel'])
    dp.register_message_handler(cancel_reg, Text(equals='cancel', ignore_case=True),
                                state='*')

    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(input_name, state=FSMAdmin.name)
    dp.register_message_handler(input_direction, state=FSMAdmin.direction)
    dp.register_message_handler(input_age, state=FSMAdmin.age)
    dp.register_message_handler(input_group, state=FSMAdmin.group)
    dp.register_message_handler(submit, state=FSMAdmin.submit)
