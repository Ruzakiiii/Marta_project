import telebot
from telebot import types


bot = telebot.TeleBot('6266914349:AAE2b-rRHp2b296_5Hwvh9khuBO9O7bP3yA')

@bot.message_handler(commands=(['start']))
def start(message):
    user_id = message.from_user.id

    key = types.ReplyKeyboardMarkup(True)

    item = types.KeyboardButton('Ребятки')

    key.add(item)

    bot.send_message(user_id, f'Привет👋 {message.from_user.first_name}\n\n Вот ссылка на видео над которым мы долго старались😇: https://www.youtube.com/@w1skeey320', reply_markup=key)


@bot.message_handler(content_types=(['text']))
def text(message):
    user_id = message.from_user.id
    if message.text == 'Ребятки':
        bot.send_message(user_id, 'Все те кто преложили свои усилия для создания этого проекта\n\n@Klixie543 \n@looop111 \n@kudryashkrrr \n@rjjbvs \n@udaleniy_akkaunt \n@Trylse \n@LastKenpachi \n@EveryOneIsNotPerfect \n@FunBoy87 \n@xcsdfe \n@eeextinct \nМаксимка \n@Meynken \n@White_F_S \n@Joker12435 \n@xkmvs \nvovan777 ')

    if message.text == message.text:
        bot.send_message(user_id,f'Привет👋 {message.from_user.first_name}\n\n Вот ссылка на видео над которым мы долго старались😇: https://www.youtube.com/@w1skeey320')

bot.polling(non_stop=True)