import telebot
from telebot import types

bot = telebot.TeleBot('1358529019:AAGAVjn4GLz1FPYXhhngS73s7ZOITOY_hpA')


@bot.message_handler(content_types=['text'])
def start_message(message):
    dictText = ['Привет', "привет", 'hi', 'hello', 'Hello']
    if message.text in dictText:
        bot.send_message(message.from_user.id,
                         "Привет, я бот для учета времени, я помогу тебе отслеживать твою активность "
                         "в социальных сетях "
                         "и не только! \n "
                         "Но пока что я работаю только с вк.")

        keyboard = types.InlineKeyboardMarkup()  # клавиатура
        key_vk = types.InlineKeyboardButton(text='VK', callback_data='VK')  # кнопка "vk"
        keyboard.add(key_vk)
        question = 'Выбери сервис для поиска страницы.'
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

    @bot.callback_query_handler(func=lambda call: True)
    def callback_worker(call):
        if call.data == "VK":  # call.data это callback_data, указанная при объявлении кнопки
            bot.send_message(message.from_user.id, "Введи свой id vk или ник.")
            bot.register_next_step_handler(message, url)

    @bot.message_handler()
    def url(message):
        id = message.text
        markup = types.InlineKeyboardMarkup()
        btn_vk_page = types.InlineKeyboardButton(text='Перейти', url=f'https://vk.com/{id}')
        btn_yes = types.InlineKeyboardButton(text='Да', callback_data='Yes')
        btn_no = types.InlineKeyboardButton(text='Нет', callback_data='No')
        markup.add(btn_vk_page, btn_yes, btn_no)
        bot.send_message(message.chat.id, f"Твоя страница? https://vk.com/{id} ", reply_markup=markup)

    @bot.callback_query_handler(func=lambda call: True)
    def callback_vk_verify(call):
        if call.data == 'Yes':
            bot.send_message(call.message.chat.id, 'Отлично!')
            # create_user(call.message.text[call.message.text.find('?')-1:])
        elif call.data == 'No':
            bot.send_message(call.message.chat.id, 'Проверь ник ещё раз, если что-то не так введи данные ещё раз')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Ок!',
                              reply_markup=None)


bot.polling(none_stop=True)
