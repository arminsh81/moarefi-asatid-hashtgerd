from telegram.ext import Updater, Filters, CommandHandler,MessageHandler, Dispatcher
from telegram import Bot
from . import temp_cred, main, conv_handler

updater = Updater(temp_cred.token)
dispatcher: Dispatcher = updater.dispatcher
bot: Bot = updater.bot


def run():
    dispatcher.add_handler(CommandHandler('start', main.start))
    dispatcher.add_handler(MessageHandler(Filters.user(temp_cred.admins_ids), conv_handler.msg_handler))
    updater.start_polling()
    print(bot.username, " Online!")
    updater.idle()
