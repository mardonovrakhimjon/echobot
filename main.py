from telegram.ext import Updater, MessageHandler, CommandHandler, Filters

from settings import settings
from handlers import (
    start,
    echo_text,
    echo_photo,
)


def main():
    updater = Updater(token=settings.TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(
        handler=CommandHandler(command='start', callback=start)
    )
    dispatcher.add_handler(
        handler=MessageHandler(filters=Filters.text, callback=echo_text)
    )
    dispatcher.add_handler(
        handler=MessageHandler(filters=Filters.photo, callback=echo_photo)
    )

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
