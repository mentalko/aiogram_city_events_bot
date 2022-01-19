from aiogram import types

from loader import dp, bot
from data.config import MODERATE_CHAT
from data.messages import LIST_TEMPLATE_MSG
from keyboards.inline.inline_keyboards import create_moderate_ik
import utils.db_api.mongo_db as db
from bson.objectid import ObjectId


async def send_moderate_msg(document):
    msg = LIST_TEMPLATE_MSG.format(document['title'], document['date'], document['place'], document['description'])
    moderate_ik = create_moderate_ik(str(document['_id']))
    print(moderate_ik)
    await bot.send_message(chat_id=MODERATE_CHAT, text=msg, reply_markup=moderate_ik, parse_mode=types.ParseMode.MARKDOWN)
    
    
@dp.callback_query_handler(lambda callback: str(callback.message.chat.id) == MODERATE_CHAT)
async def order_answer(callback_query: types.CallbackQuery):
    chat_id = callback_query.message.chat.id
    calldata = callback_query.data.split("-")
    
    if calldata[0] == 'moderate_accept':
        await bot.send_message(chat_id, 'Принято! ')
        document = {'_id': ObjectId(calldata[1]) }
        set_document = {'$set': {'is_active': True}}
        await db.do_update_one('events', document, set_document)
        
    elif calldata[0] == 'moderate_decline':
        await bot.send_message(chat_id, 'Удалено! ')
        document = {'_id': ObjectId(calldata[1]) }
        await db.do_delete_one('events', document)

