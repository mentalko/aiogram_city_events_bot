from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from keyboards.default.default_keyboards import main_kb

import data.messages as messages 
import utils.db_api.mongo_db as db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(messages.WELCOM_MSG, reply_markup=main_kb )
 