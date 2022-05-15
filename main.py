from bot import bot

from time import sleep


if __name__ == '__main__':
    while True:
        try:
            bot.polling()
        except Exception:
            sleep(1)
