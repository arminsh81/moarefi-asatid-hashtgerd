from telegram import ReplyKeyboardMarkup, KeyboardButton


def start(update, context):
    print(update)
    buttons = [
        ["معرفی اوستاد"],
        ["سرچ اوستاد"]
    ]
    markup = ReplyKeyboardMarkup(buttons, resize_keyboard=True)
    if update.effective_user.id == 660462150:
        update.effective_message.reply_text('سلاپ داش', reply_markup=markup)
    elif update.effective_user.id == 973672387:
        update.effective_message.reply_text('سلام لاو', reply_markup=markup)
