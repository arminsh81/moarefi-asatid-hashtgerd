from telegram import ReplyKeyboardMarkup
from . import texts
from .conv_handler import add_next_step


def start(update, context):
    print(update)
    user_id = update.effective_user.id
    buttons = [
        [texts.ostad_moarefi],
        [texts.ostad_search]
    ]
    markup = ReplyKeyboardMarkup(buttons, resize_keyboard=True)
    if update.effective_user.id == 660462150:
        update.effective_message.reply_text('سلاپ داش', reply_markup=markup)
    elif update.effective_user.id == 973672387:
        update.effective_message.reply_text('سلام لاو', reply_markup=markup)
    add_next_step(user_id, what_ostad)


def what_ostad(update, context):
    text = update.effective_message.text
    if text == texts.ostad_moarefi:
        update.effective_message.reply_text(texts.enter_ostad_name)
    elif text == texts.ostad_search:
        update.effective_message.reply_text(texts.enter_ostad_name_search)
    user_id = update.effective_user.id
    add_next_step(user_id, khob_ostad)


def khob_ostad(update, context):
    print(2, update)
