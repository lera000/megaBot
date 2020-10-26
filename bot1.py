from telebot import types

import telebot

bot = telebot.TeleBot('1358529019:AAGAVjn4GLz1FPYXhhngS73s7ZOITOY_hpA')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    dictText = ['Привет', "привет", 'hi', 'hello', 'Hello']

    if message.text in dictText:
        bot.send_message(message.from_user.id, "Привет, я бот, трекающий твое время.")

        keyboard = types.InlineKeyboardMarkup()  # клавиатура
        key_start = types.InlineKeyboardButton(text='Start a track', callback_data='start a track')  # кнопка "старт"
        keyboard.add(key_start)  # добавляем кнопку в клавиатуру
        key_stop = types.InlineKeyboardButton(text='Stop a track', callback_data='stop a track') # кнопка "стоп"
        keyboard.add(key_stop)
        question = 'Чем я могу тебе помочь?'
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")

    elif message.text == "/start":
        bot.send_message(message.from_user.id, "Трек начат")

    elif message.text == "/stop":
        bot.send_message(message.from_user.id, "Трек остановлен")

    elif message.text == "/report":
        bot.send_message(message.from_user.id, "Ваш трек за сегодня:")

    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

    @bot.callback_query_handler(func=lambda call: True)
    def callback_worker(call):
        if call.data == "start a track":  # call.data это callback_data, указанная при объявлении кнопки
            bot.send_message(message.from_user.id, "Трек начат")
        elif call.data == "stop a track":
            bot.send_message(message.from_user.id, "Трек остановлен")


bot.polling(none_stop=True, interval=0) # проверка ботом на сообщение
