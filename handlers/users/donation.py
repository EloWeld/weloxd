from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery, PreCheckoutQuery, ContentType, LabeledPrice

from loader import dp, bot
from middlewares.database import MainDB


@dp.callback_query_handler(text='donate')
@dp.message_handler(Command('donate'))
async def donate_hand(call: CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_invoice(chat_id=call.from_user.id,
                           title='Донатик',
                           description='Пж, хочу своей лолите купить красивое платишко. '
                                       'Скиньте денег, а то вызову на вас Резню1734',
                           payload='donate_payload',
                           provider_token='381764678:TEST:28210',
                           currency='RUB',
                           start_parameter='test_bot',
                           prices=[LabeledPrice("DONTATE FORRRR MEEEE", 6000)])


@dp.pre_checkout_query_handler()
async def process_pre_checkout_query(pcq: PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pcq.id, ok=True)


@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def process_pay(message: Message):
    if message.successful_payment.invoice_payload == 'donate_payload':
        await message.answer(text='Ураааа!!! Спасибо за донатик! Ты лапочка ♥\n'
                                  'Подписка подключена')
        MainDB.update_subscription(id=message.from_user.id, subscription=1)