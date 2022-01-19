from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from keyboards.default.default_keyboards import main_kb
from utils.models.user import User

import data.messages as messages 
import utils.db_api.mongo_db as db

async def user_is_exists(id: int) -> bool:
    if await db.do_find_one('users', {'id': id}):
        return True
    else: 
        return False
    


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    
    if not await user_is_exists(message.from_user.id):
        new_user = User(id=message.from_user.id, 
                        username=message.from_user.username,
                        events=[]
                        )
        
        await db.do_insert_one('users', new_user)
    
    await message.answer(messages.WELCOM_MSG, reply_markup=main_kb )
 