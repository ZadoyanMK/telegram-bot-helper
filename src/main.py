from telegram.ext import Updater, CommandHandler
import telegram
import requests
from lxml import html
import random
import logging


def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url


def get_second_url():
    page = requests.get('https://www.pornpics.com/pornstar/')
    tree = html.fromstring(page.content)
    urls = tree.xpath('//a[contains(@class, "rel-link")]/img/@src')
    url = random.choice(urls)
    return url


def bop(bot, update):
    chat_id = update.message.chat_id
    bot.send_chat_action(chat_id=chat_id, action=telegram.ChatAction.UPLOAD_PHOTO)
    url = get_url()
    bot.send_photo(chat_id=chat_id, photo=url)
    # bot.send_message(chat_id=chat_id, text="test")


def t(bot, update):
    chat_id = update.message.chat_id
    bot.send_chat_action(chat_id=chat_id, action=telegram.ChatAction.UPLOAD_PHOTO)
    url = get_second_url()
    bot.send_photo(chat_id=chat_id, photo=url)


def main():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    updater = Updater('859269592:AAFCO36kDjNP_LNHAq9xFlb4O_4rkY-B-U0')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop', bop))
    dp.add_handler(CommandHandler('t', t))
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
