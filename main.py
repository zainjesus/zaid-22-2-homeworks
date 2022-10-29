import asyncio
from aiogram.utils import executor
from config import dp
import logging
from handlers import client, callback, extra, fsmAdminMentor, admin, notifications, inline
from database.bot_db import sql_create


async def on_startup(_):
    asyncio.create_task(notifications.scheduler())
    sql_create()


client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
fsmAdminMentor.register_handlers_fsm_admin(dp)
admin.register_handlers_admin(dp)
notifications.register_handlers_notification(dp)
inline.register_handler_inline(dp)
extra.register_handlers_extra(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
