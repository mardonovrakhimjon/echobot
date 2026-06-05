import json
from telegram.ext import CallbackContext
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton

from messages import messages


USERS_FILE = "users.json"

def start(update: Update, context: CallbackContext):
    save_user(update)
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


def save_user(update):
    if not update.message or not update.message.from_user:
        return
        
    user_id = update.message.from_user.id
    username = update.message.from_user.username
    first_name = update.message.from_user.first_name

    file = open("users.json", "r", encoding="utf-8")
    users = json.load(file)
    file.close()

    exists = False
    for u in users:
        if u["user_id"] == user_id:
            exists = True

    if not exists:
        new_user = {
            "user_id": user_id,
            "username": username,
            "first_name": first_name
        }
        users.append(new_user)
        
        file = open("users.json", "w", encoding="utf-8")
        json.dump(users, file, indent=4, ensure_ascii=False)
        file.close()

def start_funksiyasi(message):
    
    save_user(message.from_user.id, message.from_user.username, message.from_user.first_name)