import os
import random

from environs import env
import telegram


def send_message(bot, chat_id):
    bot.send_message(
        chat_id=chat_id,
        text="I'm sorry Dave I'm afraid I can't do that."
    )


def send_picture(bot, chat_id):
    files = os.listdir('images')
    file = random.choice(files)
    path = f'images/{file}'

    bot.send_photo(
        chat_id=chat_id,
        photo=open(path, 'rb')
    )


def main():
    env.read_env()
    tg_token = env('BOT_TOKEN')
    chat_id = env('CHAT_ID')
    bot = telegram.Bot(token=tg_token)

    # send_message(bot, chat_id)
    send_picture(bot, chat_id)


if __name__ == '__main__':
    main()
