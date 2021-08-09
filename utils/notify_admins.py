import logging

from aiogram import Dispatcher, types

from data.config import admins
from handlers.users.start import bot_start


async def on_startup_notify(dp: Dispatcher):
    for admin in admins:
        try:
            await dp.bot.send_message(admin, "Weloxed Bot started", disable_notification=True)
        except Exception as err:
            logging.exception(err)
