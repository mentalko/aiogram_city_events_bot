from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


main_kb = ReplyKeyboardMarkup(resize_keyboard=True).row(KeyboardButton('Посмотреть афишу'),
            KeyboardButton('Мои записи')).add(KeyboardButton('Разместить мероприятие'))

cancel_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('Отмена'))


accept_kb = InlineKeyboardMarkup().row(InlineKeyboardButton('Принять', callback_data='answer_accept'),
                                             InlineKeyboardButton('Отклонить', callback_data='answer_dismiss'))


event_list_kb = InlineKeyboardMarkup().row(InlineKeyboardButton('Пойду!', callback_data='answer_imgoing'),
                                             InlineKeyboardButton('Не интересно', callback_data='answer_notinteresting'))