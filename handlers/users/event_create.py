import json
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text

from data.messages import LIST_TEMPLATE_MSG
from loader import dp, bot
from keyboards.default.default_keyboards import main_kb, cancel_kb, accept_kb
from data.config import MODERATE_CHAT
import utils.db_api.mongo_db as db

class FSMEvent(StatesGroup):
    title = State()
    date = State()
    place = State()
    description = State()

@dp.message_handler(Text(equals="Отмена"), state="*")
@dp.message_handler(state="*", commands='cancel')
async def set_description(message: types.Message, state: FSMContext):
    current_state = state.get_state()
    if current_state == None:
        return
    await state.finish()
    await message.answer('Процесс создания прерван!', reply_markup=main_kb)

#Начало диалога создания мероприятия
@dp.message_handler(text="Разместить мероприятие")
@dp.message_handler(commands='create', state=None)
async def start_create_event(message: types.Message):
    await FSMEvent.first()
    await message.answer("Название:", reply_markup=cancel_kb)


@dp.message_handler(state=FSMEvent.title)
async def set_title(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["title"] = message.text
    await FSMEvent.next()
    await message.answer(f"Хорошо, теперь дату проведения:\n"
                         f'Например:\n "20.01", "20 января" ')

@dp.message_handler(state=FSMEvent.date)
async def set_date(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["date"] = message.text
    await FSMEvent.next()
    await message.answer(f"Теперь название места либо адрес:\n"
                         f'Например:\n "ДК", "306 квадратов", "Скуратов на ул. Интернациональная,35" ')

@dp.message_handler(state=FSMEvent.place)
async def set_place(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["place"] = message.text
    await FSMEvent.next()
    await message.answer(f"И напоследок короткое или длинное описание:")


@dp.message_handler(state=FSMEvent.description)
async def set_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["description"] = message.text
    async with state.proxy() as data:
        # await message.answer(str(data))
        print(MODERATE_CHAT)
        
        document = { 
            "title": data["title"], 
            "date": data["date"],
            "place": data["place"], 
            "description": data["description"],
            "is_active": 'False',
            }
        
        await db.do_insert_one('events', document)
        msg = LIST_TEMPLATE_MSG.format(document['title'], document['date'], document['place'], document['description'])
        await bot.send_message(chat_id=MODERATE_CHAT, text=msg, reply_markup=accept_kb)
        
        
    await message.answer(f"Отлично, отправленно на модерацию:", reply_markup=main_kb)
    await state.finish()


