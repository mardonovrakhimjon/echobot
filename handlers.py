from telegram.ext import CallbackContext
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton

from messages import messages


def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        messages["start"].format(update.message.from_user.full_name),
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="Bosh Sahifa"),
                    KeyboardButton(text="Mahsulotlar"),
                ]
            ],
            resize_keyboard=True,
        ),
    )


def echo_text(update: Update, context: CallbackContext):
    update.message.reply_text(update.message.text)


def echo_photo(update: Update, context: CallbackContext):
    update.message.reply_photo(update.message.photo[0])


def main_menu(update: Update, context: CallbackContext):
    update.message.reply_text("Bosh sahifaga kirdingiz")


def products_menu(update: Update, context: CallbackContext):
    update.message.reply_text("Mahsulotlar sahifaga kirdingiz")
