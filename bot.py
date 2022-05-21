import telebot
from tok import api
from typing import NoReturn
import traceback
import os

class Bot:
    bot = telebot.TeleBot(token=api)
    def __init__(self):
        super().__init__()
        self.handler()

    def handler(self):
        bot = self.bot
        @bot.message_handler(commands=['start'])
        def start(message):
            user_first_name = str(message.chat.first_name)
            bot.send_message(message.chat.id, f'Приветствую тебя, {user_first_name}! 🎵 \nНас объединяет одно - любовь к музыке! 🧡 \nНаш бот предлагает тебе 1000+ треков разного жанра и настроения. \nВсё это - совершенно БЕСПЛАТНО! 🙅 \n')
            with open('attachments/photo/welcome.jpg', 'rb') as f:
                 welcome_photo = f.read()
                 bot.send_photo(message.chat.id, welcome_photo)


        @bot.message_handler(content_types=['text'])
        def get_text(message):
            import req
            bot.send_message(message.chat.id, 'Секунду... ⏳')
            song_num = req.request.download_music(message.text)
            try:
                with open('attachments/audio/' + song_num + '.mp3', 'rb') as f:
                    song = f.read()
                    bot.send_audio(message.chat.id, song)
                    path = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                        'attachments/audio/' + song_num + '.mp3')
                    os.remove(path)

            except Exception:
                print(traceback.format_exc())
                bot.send_message(message.chat.id, 'Упсс.. К сожалению у нас нет этого трека. Мы работаем над этим! ⚠️')

while True:
    try:
        if __name__ == '__main__':
            b = Bot()
            b.bot.polling(none_stop=True, interval=0)
        continue
    except Exception:
        continue