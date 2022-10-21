import sqlite3
import random
from config import bot


def sql_create():
    global db, cursor
    db = sqlite3.connect("bot.sqlite3")
    cursor = db.cursor()

    if db:
        print('База данных подключена!')

    db.execute("CREATE TABLE IF NOT EXISTS mentors"
               "(id INTEGER PRIMARY KEY, name TEXT, direction TEXT, age INTEGER, "
               "group_ TEXT)")
    db.commit()


async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO mentors VALUES (?, ?, ?, ?, ?)", tuple(data.values()))
        db.commit()


async def sql_command_random(message):
    results = cursor.execute("SELECT * FROM mentors").fetchall()
    random_user = random.choice(results)
    await bot.send_message(message.from_user.id, f"id ментора - {random_user[0]} \nИмя ментора - {random_user[1]}"
                                                 f" \nНаправление ментора - {random_user[2]}"
                                                 f" \nВозраст ментора - {random_user[3]} \nГруппа ментора - "
                                                 f"{random_user[4]}")


async def sql_command_all():
    return cursor.execute("SELECT * FROM mentors").fetchall()


async def sql_command_delete(id):
    cursor.execute("DELETE FROM mentors WHERE id = ?", (id,))
    db.commit()
