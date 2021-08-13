import asyncio

from aiogram import types


async def del_message(message: types.Message, time_in_milliseconds: int):
    await asyncio.sleep(time_in_milliseconds)
    await message.delete()
