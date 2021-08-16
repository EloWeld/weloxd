from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import backend

inline_start_menu = InlineKeyboardMarkup(inline_keyboard=[
      [
            InlineKeyboardButton(text='Задонатте мне, пж', callback_data='donate'),
      ]
  ])

