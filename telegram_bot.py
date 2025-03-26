from environs import env
import telegram


def get_message(bot, chat_id):
    bot.send_message(
        chat_id=chat_id,
        text="I'm sorry Dave I'm afraid I can't do that."
    )


def main():
    env.read_env()
    tg_token = env('BOT_TOKEN')
    chat_id = env('CHAT_ID')
    bot = telegram.Bot(token=tg_token)

    get_message(bot, chat_id)


if __name__ == '__main__':
    main()
