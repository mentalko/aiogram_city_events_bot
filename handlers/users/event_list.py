from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from bson import ObjectId

from loader import dp, bot
from data.messages import LIST_TEMPLATE_MSG
from keyboards.inline.inline_keyboards import create_event_list_ik, cancel_event_list_ik
import utils.db_api.mongo_db as db


#Начало диалога создания мероприятия
@dp.message_handler(text="Посмотреть афишу")
async def event_list(message: types.Message):
    rows = await db.do_find('events',  {'is_active': True})
    for row in rows:
        msg = LIST_TEMPLATE_MSG.format(row['title'], row['date'], row['place'], row['description'])
        await message.answer(msg, reply_markup=create_event_list_ik(row['_id']),  parse_mode=types.ParseMode.MARKDOWN)
        
    
@dp.callback_query_handler(lambda callback: callback.data.split('_')[0] == 'answer')
async def list_event_answer(callback_query: types.CallbackQuery):
    chat_id = callback_query.message.chat.id
    user_id = callback_query.from_user.id
    calldata = callback_query.data.split("-")
    
    if calldata[0] == 'answer_imgoing':
        await bot.send_message(chat_id, 'Вы записались!')
        document = {'id': user_id }
        set_document = {'$push': {'events': ObjectId(calldata[1])}}
        await db.do_update_one('users', document, set_document)
    elif calldata[0] == 'answer_notinteresting':
        await bot.send_message(chat_id, 'Функционал еще в разработке!')


@dp.message_handler(text="Мои записи")
async def my_list(message: types.Message):
    events = await db.do_find_one('users',  {'id': message.from_user.id})
    if not events['events']:
        await message.answer('Вы никуда еще не записались!')
        
    for event in events['events']:
        row = await db.do_find_one('events', {'_id': event})
        msg = LIST_TEMPLATE_MSG.format(row['title'], row['date'], row['place'], row['description'])
        await message.answer(msg, reply_markup=cancel_event_list_ik(row['_id']),  parse_mode=types.ParseMode.MARKDOWN)
     
     
@dp.callback_query_handler(lambda callback: callback.data.split('-')[0] == 'cancel')
async def list_event_answer(callback_query: types.CallbackQuery):
    chat_id = callback_query.message.chat.id
    user_id = callback_query.from_user.id
    calldata = callback_query.data.split("-")
    
    if calldata[0] == 'cancel':
        await bot.send_message(chat_id, 'Запись отменена! ')
        document = {'id': user_id }
        unset_document = {'$pull': {'events': ObjectId(calldata[1])}}
        await db.do_update_one('users', document, unset_document)
        