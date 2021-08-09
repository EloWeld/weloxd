from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


reply_start_menu = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
      [
            KeyboardButton(text='Котики'),
            KeyboardButton(text='Задание'),
            KeyboardButton(text='Аниме'),
      ],
      [
            KeyboardButton(text='Zalgo'),
            KeyboardButton(text='Музло'),
            KeyboardButton(text='Помощь'),
      ]
  ])

zalgo_menu = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
      [
            KeyboardButton(text='1️⃣'),
            KeyboardButton(text='2️⃣'),
            KeyboardButton(text='3️⃣'),
      ],
      [
            KeyboardButton(text='🛑STOP🛑')
      ]
  ])
