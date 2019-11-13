import telebot
import botvk


token_tel = '1061438177:AAF-LO2jVpex46IxaErTMYyODpvfPHXsK3Y'
bot = telebot.TeleBot(token_tel)
keyboard1 = telebot.types.ReplyKeyboardMarkup(row_width=100, resize_keyboard=True)
keyboard1.row('Привет', 'Пока', 'Ласт пост')
keyboard1.row('/json', '/start', 'Я тебя люблю')
# resize_keyboard=True, one_time_keyboard=True


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)


@bot.message_handler(commands=['json'])
def start(message):
    bot.send_message(message.chat.id, str(message))


@bot.message_handler(commands=['chat_id'])
def chat_id(message):
    bot.send_message(message.chat.id, chat_id)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')
    elif message.text.lower() == 'я тебя люблю':
        bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')
    elif message.text.lower() == 'ласт пост':
        bot.send_message(message.chat.id, botvk.take_posts()[0]['text'])
        album = []
        for msg in botvk.take_posts()[0]['attachments']:
            album.append(msg['photo']['sizes'][-1]['url'])
        bot.send_media_group(message.chat.id, album)


@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)


bot.polling()
