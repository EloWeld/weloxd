import logging

from aiogram import Dispatcher

import nav
from src.data.config import admins


async def on_startup_notify(dp: Dispatcher):
    for admin in admins:
        try:
            await dp.bot.send_message(admin, "Weloxed Bot started", disable_notification=True,
                                      reply_markup=nav.reply_markups.base_menu)
        except Exception as err:
            logging.exception(err)
