import telebot
import config
from telebot import types
from cov import getcorona

bot = telebot.TeleBot(config.token)

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Коронавирус")
item2 = types.KeyboardButton("Начать диалог")
markup.add(item1, item2)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIfZl9_JejD_V_wc6qkAdxMVrpr4cqAAAIuAQACIpHMAztF5TszquAQGwQ', reply_markup=markup)
    #bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы быть пожилым сычем.".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)
 
@bot.message_handler(content_types=['text'])
def lalala(message):
        if message.text == 'Коронавирус':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.row('сша', 'россия', 'италия','япония')
            bot.send_message(message.chat.id, "Выберите страну:",
        parse_mode='html', reply_markup=markup)
            bot.register_next_step_handler(message, choosecountry)
        elif message.text == 'Начать диалог':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.row('Привет', 'Закончить Диалог')
            bot.send_message(message.chat.id, "", reply_markup=markup)
        elif message.text == 'Привет':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.row('Как тебя зовут?', 'Закончить Диалог')
            bot.send_message(message.chat.id, "Привет, {0.first_name}!".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)
        elif message.text == 'Как тебя зовут?':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.row('😊 Как у тебя дела?', 'Закончить Диалог')
            bot.send_message(message.chat.id, "Я - <b>{1.first_name}</b>".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)
        elif message.text == 'Закончить Диалог':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Коронавирус")
            item2 = types.KeyboardButton("Начать диалог")
            markup.add(item1, item2)
            bot.send_message(message.chat.id, 'До свидания, с вами было приятно общаться!', reply_markup=markup)
        elif message.text == '😊 Как у тебя дела?':
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
            item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')
            markup.add(item1, item2)
            bot.send_message(message.chat.id, 'Отлично, сам как?', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')
 
def choosecountry(message):
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIgT1-A4QeHcYRTjLeh7Q35tkpYaU2IAAIZBgACu-LZS7x-ZyzJUUkPGwQ')
    bot.send_message(message.chat.id, getcorona(message.text), reply_markup=markup)

"""@bot.message_handler(content_types= ['text'])
def corona(message):
    final_message = ""
    get_message_bot = message.text.strip().lower()
    if get_message_bot == "сша":
        location = covid19.getLocationByCountryCode("US")
    elif get_message_bot == "россия":
        location = covid19.getLocationByCountryCode("RU")
    elif get_message_bot == "япония":
        location = covid19.getLocationByCountryCode("JP")
    elif get_message_bot == "италия":
        location = covid19.getLocationByCountryCode("IT")
    else:
        location = covid19.getLatest()
        final_message = f"<u>Данные по всему миру:</u>\n<b>Заболевшие: </b>{location['confirmed']}"

    if final_message == "":
        date = location[0]['last_updated'].split("T")
        time = date[1].split(".")
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIgT1-A4QeHcYRTjLeh7Q35tkpYaU2IAAIZBgACu-LZS7x-ZyzJUUkPGwQ')
        final_message = f"<u>Данные по стране:</u>\nНаселение: {location[0]['country_population']:,}\n" \
				f"Последнее обновление: {date[0]} {time[0]}\nПоследние данные:\n<b>" \
				f"Заболевших: </b>{location[0]['latest']['confirmed']:,}\n<b>Сметрей: </b>" \
				f"{location[0]['latest']['deaths']:,}"

    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)"""

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Вот и отличненько 😊')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Бывает 😢')
 
            #bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="😊 Как дела?", reply_markup=None)
 
            #bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!!11")
 
    except Exception as e:
        print(repr(e))

if __name__ == '__main__':
     bot.polling(none_stop=True)