from telegram.ext import Updater, CommandHandler
from telegram import Contact
import requests
import re


def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url


def bop(bot, update):
    url = get_url()
    chat_id = update.message.chat_id
    print('*' * 10)
    print(chat_id)
    print('*' * 10)
    bot.send_photo(chat_id=chat_id, photo=url)
    # bot.send_message(chat_id=chat_id, text="test")


def main():
    updater = Updater('859269592:AAFCO36kDjNP_LNHAq9xFlb4O_4rkY-B-U0')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop', bop))
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
