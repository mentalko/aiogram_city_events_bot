from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_kb = ReplyKeyboardMarkup(resize_keyboard=True).row(KeyboardButton('Посмотреть афишу'),
            KeyboardButton('Мои записи')).add(KeyboardButton('Разместить мероприятие'))

cancel_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('Отмена'))

