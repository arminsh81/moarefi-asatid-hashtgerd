from telegram.ext import Updater, Filters, CommandHandler, Dispatcher
from telegram import Bot
from . import temp_cred, main

updater = Updater(temp_cred.token)
dispatcher: Dispatcher = updater.dispatcher
bot: Bot = updater.bot


def run():
    dispatcher.add_handler(CommandHandler('start', main.start))
    updater.start_polling()
    print(bot.username, " Online!")
    updater.idle()
