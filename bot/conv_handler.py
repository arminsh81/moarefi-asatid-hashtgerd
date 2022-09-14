conv_waiters = {}

from re import match


def handler_helper(update, context, handlers, rem):
    update.callback_query.data = update.callback_query.data.replace(rem, '', 1)
    data = update.callback_query.data
    for regex, handler in handlers.items():
        if match(regex, data):
            return handler(update, context)


def add_next_step(user_id, function):
    conv_waiters[user_id] = function


def del_steps(user_id):
    try:
        conv_waiters.pop(user_id)
    except:
        pass


def msg_handler(update, context):
    handler = conv_waiters.get(update.effective_user.id)
    # if handler and update.message.chat.type == 'private':
    return handler(update, context)
