import os
from aiogram import executor

from loader import dp, bot
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from utils.db_api.mongo_db import check_db_exists
from data.config import WEBHOOK_URL


async def on_startup(dispatcher):
    
    await bot.set_webhook(WEBHOOK_URL)
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)

    # Уведомляет про запуск
    await on_startup_notify(dispatcher)
    
    await check_db_exists()
    
async def on_shutdown(dispatcher):
    await bot.delete_webhook()




if __name__ == '__main__':
    # executor.start_polling(dp, on_startup=on_startup)
    executor.start_webhook(
    dispatcher=dp,
    webhook_path='',
    on_startup=on_startup,
    on_shutdown=on_shutdown,
    skip_updates=True,
    host='0.0.0.0',
    port=int(os.environ.get('PORT', 5000))
)
