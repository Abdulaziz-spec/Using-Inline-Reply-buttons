from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
# InlineKeyboardMarkup - Класс для создания области для кнопок
# InlineKeyboardButton - Класс для создания кнопки
from config import VIDEOS



def videos_keyboard():
    markup = InlineKeyboardMarkup(row_width=2)
    buttons = []

    for key, data in VIDEOS.items():
        title = data['title']
        callback_data = f'video_{key}'
        button = InlineKeyboardButton(text=title, callback_data=callback_data)
        buttons.append(button)

    markup.add(*buttons)
    return markup
