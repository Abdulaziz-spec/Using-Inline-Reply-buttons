from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def menu_buttons():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)  # Создали область под кнопки
    btn1 = KeyboardButton(text='Список Видео Курсов')  # Создали Кнопку
    markup.add(btn1)
    return markup