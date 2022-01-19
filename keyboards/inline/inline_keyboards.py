from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# button_list.append(InlineKeyboardButton(each, callback_data = each))

def create_moderate_ik(id):
    moderate_ik = InlineKeyboardMarkup().row(InlineKeyboardButton('Принять', callback_data='moderate_accept-{}'.format(id)),
                                                InlineKeyboardButton('Отклонить', callback_data='moderate_decline-{}'.format(id)))
    return moderate_ik

def create_event_list_ik(id):
    event_list_ik = InlineKeyboardMarkup().row(InlineKeyboardButton('Пойду!', callback_data='answer_imgoing-{}'.format(id)),
                                                InlineKeyboardButton('Не интересно', callback_data='answer_notinteresting-{}'.format(id)))
    return event_list_ik


def cancel_event_list_ik(id):
    cancel_list_ik = InlineKeyboardMarkup().add(InlineKeyboardButton('Отказаться от участия!', callback_data='cancel-{}'.format(id)))
    return cancel_list_ik