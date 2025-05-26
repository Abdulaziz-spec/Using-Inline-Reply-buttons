from telebot import TeleBot
from telebot.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv
import os
from Reply import VIDEOS
from Reply import videos_keyboard
from buttons import menu_buttons

load_dotenv()
bot = TeleBot(os.getenv("TOKEN"))


@bot.callback_query_handler(func=lambda call: call.data.startswith('video_'))
def handle_video_callback(call):
    video_key = call.data.split('_')[1]

    video = VIDEOS.get(video_key)
    if video:
        bot.send_message(call.message.chat.id, f"🎬 {video['title']}\nСмотреть: {video['url']}")
    else:
        bot.send_message(call.message.chat.id, "Видео не найдено.")

    bot.answer_callback_query(call.id)


@bot.message_handler(commands=['start'])
def send_start_list(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, text="Здраствуйте Вас приветсвует Бот Который Вам Отправляет Список Курсов",
                     reply_markup=menu_buttons())


@bot.message_handler(regexp='Список Видео Курсов')
def send_video_list(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, text='Выберите курс:', reply_markup=videos_keyboard())


@bot.message_handler(commands=['pass'])
def send_start_list(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, text="это мой гитхаб https://github.com/Abdulaziz-spec",
                     reply_markup=menu_buttons())


bot.infinity_polling()
