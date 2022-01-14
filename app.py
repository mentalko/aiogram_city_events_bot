from aiogram import executor

from loader import dp
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from utils.db_api.mongo_db import check_db_exists


async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)

    # Уведомляет про запуск
    await on_startup_notify(dispatcher)
    
    await check_db_exists()
    
async def on_shutdown(dispatcher):
    pass


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)

