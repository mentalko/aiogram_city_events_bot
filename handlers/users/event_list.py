from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text

from loader import dp
from data.messages import LIST_TEMPLATE_MSG
from keyboards.default.default_keyboards import main_kb, cancel_kb, event_list_kb
import utils.db_api.mongo_db as db


#Начало диалога создания мероприятия
@dp.message_handler(text="Посмотреть афишу")
async def event_list(message: types.Message):
    await message.answer("Вот все эвенты какими я располагаю:", reply_markup=main_kb)

    rows = await db.do_find('events',  {})
    

    for row in rows:
        msg = LIST_TEMPLATE_MSG.format(row['title'], row['date'], row['place'], row['description'])
        await message.answer(msg, reply_markup=event_list_kb)
        
    