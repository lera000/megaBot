import telebot
from telebot import types
from telebot.types import ReplyKeyboardMarkup

bot = telebot.TeleBot('1358529019:AAGAVjn4GLz1FPYXhhngS73s7ZOITOY_hpA')


@bot.message_handler(content_types=['text'])
def start_message(message):
    dictText = ['Привет', "привет", 'hi', 'hello', 'Hello']
    if message.text in dictText:
        bot.send_message(message.chat.id,
                         "Привет, я бот для учета времени, я помогу тебе отслеживать твою активность "
                         "в социальных сетях и не только!")

        keyboard = types.InlineKeyboardMarkup()  # клавиатура
        key_vk = types.InlineKeyboardButton(text='VK', callback_data='VK')  # кнопка "vk"
        keyboard.add(key_vk)
        key_urfu = types.InlineKeyboardButton(text='Personal account UrFU', callback_data='Personal account UrFU')
        keyboard.add(key_urfu)
        key_git = types.InlineKeyboardButton(text='GitHub', callback_data='GitHub')  # кнопка "git"
        keyboard.add(key_git)
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
            bot.register_next_step_handler(message, url_vk)

        if call.data == "Personal account UrFU":
            bot.send_message(message.from_user.id, "Введи свой логин.")
            bot.register_next_step_handler(message, url_urfu)

        if call.data == "GitHub":
            bot.send_message(message.from_user.id, "Введи свой логин.")
            bot.register_next_step_handler(message, url_git)

        if call.data == 'Yes':
            bot.send_message(call.message.chat.id, 'Отлично!')
            # create_user(call.message.text[call.message.text.find('?')-1:])
        elif call.data == 'No':
            bot.send_message(call.message.chat.id, 'Проверь ник ещё раз, если что-то не так введи данные ещё раз')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Ок!',
                              reply_markup=None)

    @bot.message_handler()
    def url_urfu(message):
        bot.send_message(message.chat.id, 'Введи свой пароль.')

    @bot.message_handler()
    def url_vk(message):
        id = message.text
        markup = types.InlineKeyboardMarkup()
        btn_vk_page = types.InlineKeyboardButton(text='Перейти', url=f'https://vk.com/{id}')
        btn_yes = types.InlineKeyboardButton(text='Да', callback_data='Yes')
        btn_no = types.InlineKeyboardButton(text='Нет', callback_data='No')
        markup.add(btn_vk_page, btn_yes, btn_no)
        bot.send_message(message.chat.id, f"Твоя страница? https://vk.com/{id} ", reply_markup=markup)

    def url_git(message):
        id = message.text
        markup = types.InlineKeyboardMarkup()
        bot.send_message(message.chat.id, 'Введи свой пароль.')


bot.polling(none_stop=True)
