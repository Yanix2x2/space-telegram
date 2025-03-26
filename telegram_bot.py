import os
import random
import time
import argparse

from environs import env
import telegram


def send_picture(bot, chat_id):
    path = []
    for address, dirs, files in os.walk('images'):
        for file in files:
            path.append(os.path.join(address, file))

    random.shuffle(path)
    bot.send_photo(
        chat_id=chat_id,
        photo=open(random.choice(path), 'rb')
    )


def main():
    env.read_env()
    tg_token = env('BOT_TOKEN')
    chat_id = env('CHAT_ID')
    bot = telegram.Bot(token=tg_token)

    parser = argparse.ArgumentParser(
            description='Время автоматической публикации'
        )
    parser.add_argument(
        '--time', 
        '-t',
        type=int,
        help='Время в секундах',
        default='4 * 3600'
    )
    args = parser.parse_args()
    print(args.time)

    while True:
        time.sleep(args.time)
        send_picture(bot, chat_id)


if __name__ == '__main__':
    main()
