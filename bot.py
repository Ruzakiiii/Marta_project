import telebot
from telebot import types
import database
import random

bot = telebot.TeleBot('6266914349:AAE2b-rRHp2b296_5Hwvh9khuBO9O7bP3yA')

@bot.message_handler(commands=(['start']))
def start(message):
    user_id = message.from_user.id

    key = types.ReplyKeyboardMarkup(True)

    item = types.KeyboardButton('Ребятки')

    key.add(item)

    bot.send_message(user_id, f'Привет👋 {message.from_user.first_name}\n\nВот ссылка на видео над которым мы долго старались😇: https://www.youtube.com/@w1skeey320', reply_markup=key)

    key1 = types.InlineKeyboardMarkup(row_width=1)

    items = types.InlineKeyboardButton(text='Получить видео✅', callback_data='Получить видео')

    key1.add(items)

    bot.send_message(user_id, '⬇️Для получения оригинального видео нажмите на кнопку ниже⬇️', reply_markup=key1)


@bot.message_handler(commands=(['start_raffle']))
def raffle(message):
    user_id = message.from_user.id

    ac = database.check_user_two()

    num = []

    all_user = []

    for i in ac:
        num.append(i[3])

        all_user.append(i[0])

        x = random.randint(0, len(num) - 1)

        vin_num = num[x]


    vin_nums = database.get_vin_num(vin_num)

    viner = []

    for i in vin_nums:
        viner.append(i[0])

    for all in all_user:
        bot.send_message(int(all), f'🎊Победил номер: {vin_num}🎊')

    bot.send_message(int(viner[0]), f'🥳Вы победили🥳\n\nВаш номер: {vin_num} оказался самым счастливым\n\n🎉Поздравляем🎉   ')




@bot.message_handler(commands=(['raffle']))
def raffle(message):
    user_id = message.from_user.id

    check = database.check_user()

    if user_id not in check:

        a = random.randrange(0, 101)

        database.add_table(user_id, message.from_user.username, message.from_user.first_name, a)

        bot.send_message(user_id, f'✨{message.from_user.first_name} теперь ты участник розыгрыша✨\n\n👾Это твой победный номер: {a}👾\n\n🤩Если твой номер окажется выигрышным мы сообщи тебе об этом🤩\n\n🤞Желаем удачи!🤞')

    elif user_id in check:
        bot.send_message(user_id, f'Вы уже участвуете в розыгрыше')


@bot.message_handler(content_types=(['text']))
def text(message):
    user_id = message.from_user.id
    if message.text == 'Ребятки':
        bot.send_message(user_id, 'Все те кто преложили свои усилия для создания этого проекта\n\n@Klixie543 \n@looop111 \n@kudryashkrrr \n@rjjbvs \n@udaleniy_akkaunt \n@Trylse \n@LastKenpachi \n@EveryOneIsNotPerfect \n@FunBoy87 \n@xcsdfe \n@eeextinct \nМаксимка \n@Meynken \n@White_F_S \n@Joker12435 \n@xkmvs \nvovan777 ')

    elif message.text == message.text:
        bot.send_message(user_id,f'Привет👋 {message.from_user.first_name}\n\n Вот ссылка на видео над которым мы долго старались😇: https://www.youtube.com/@w1skeey320')


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.message:
        if call.data == 'Получить видео':
            bot.send_video(call.from_user.id, 'BAACAgIAAxkBAAPCZAein5rGPUjhOwfwL2qdPaJjD4sAAqckAAJAvhhIUrZPUNV7zeAuBA',caption='✅Это оригинальное видео✅')

print('bot start')
bot.polling(non_stop=True)