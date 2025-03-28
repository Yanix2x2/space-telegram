import os
import random
import time
import argparse
from dotenv import load_dotenv

import telegram

from helper import walk_directory


def send_picture(bot, chat_id, directory):
    paths = walk_directory(directory)
    random.shuffle(paths)
    with open(random.choice(paths), 'rb') as photo:
        bot.send_photo(
            chat_id=chat_id,
            photo=photo
        )


def main():
    load_dotenv()
    tg_token = os.environ['TELEGRAM_BOT_TOKEN']
    chat_id = os.environ['TELEGRAM_CHAT_ID']

    bot = telegram.Bot(token=tg_token)

    parser = argparse.ArgumentParser(description='Telegram bot')
    parser.add_argument('--time', '-t', type=int, help='Время в секундах', default='14400')
    parser.add_argument('--directory', '-d', help='Директория для поиска', default='images')
    args = parser.parse_args()

    while True:
        try:
            send_picture(bot, chat_id, args.directory)
            time.sleep(args.time)
        except telegram.error.NetworkError as err:
            print(f"Ошибка подключения: {err}, повтор через 5 секунд")
            time.sleep(5)


if __name__ == '__main__':
    main()
