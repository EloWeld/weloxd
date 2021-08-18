from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


base_menu = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
      [
            KeyboardButton(text='Котики'),
            KeyboardButton(text='Задание'),
            KeyboardButton(text='🕶Смотрелка🎞'),
            KeyboardButton(text='Погода'),
      ],
      [
            KeyboardButton(text='Текст-стилист'),
            KeyboardButton(text='Музло'),
            KeyboardButton(text='Кричалка на юзеров'),
            KeyboardButton(text='Помощь'),
      ]
  ])

cities_menu = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
      [
            KeyboardButton(text='Лондон'),
            KeyboardButton(text='Мытищи'),
            KeyboardButton(text='Самара'),
            KeyboardButton(text='Набережные Челны'),
      ],
      [
            KeyboardButton(text='Нидерланды'),
            KeyboardButton(text='Латвия'),
            KeyboardButton(text='Казань'),
            KeyboardButton(text='Тула'),
      ],
      [
            KeyboardButton(text='🛑STOP🛑')
      ]
  ])


exit_menu = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
      [
            KeyboardButton(text='🛑STOP🛑'),
      ]
  ])

viewer_menu = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
      [
            KeyboardButton(text='😎Аниме😎'),
            KeyboardButton(text='😐Фильм😐'),
      ],
      [
            KeyboardButton(text='🛑STOP🛑')
      ]
])

broadcasting_menu = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
      [
            KeyboardButton(text='🌼 Закрыть варежку и сдохнуть 🌸'),
      ]
  ])