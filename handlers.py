from telegram.ext import CallbackContext
from telegram import Update

from messages import messages


def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        messages['start'].format(update.message.from_user.full_name)
    )


def echo_text(update: Update, context: CallbackContext):
    update.message.reply_text(update.message.text)


def echo_photo(update: Update, context: CallbackContext):
    update.message.reply_photo(update.message.photo[0])
