from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from src.data.config import admins


class IsAdmin(BoundFilter):
    async def check(self, message: types.Message, *args) -> bool:
        member = message.from_user.id in admins
        return member