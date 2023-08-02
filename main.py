from telegram.ext import (
    Application)

from env.env import config

from main_project.commands import start_handler, help_handler, custom_handler,  caps_handler
from main_project.handlers import error, msg_handler, echo_handler, test_handler


API_TOKEN = config("API_TOKEN", default=None)
BOT_USERNAME = config("BOT_USERNAME", default=None)
BOT_NAME=config("BOT_NAME", default=None)


if __name__ == '__main__':
    print("BUILDING APP")
    app = Application.builder().token(API_TOKEN).build()

    print("SETTING COMMANDS")
    app.add_handler(start_handler)
    app.add_handler(help_handler)
    app.add_handler(custom_handler)
    app.add_handler(caps_handler)

    print("SETTING MSG HANDLER")
    app.add_handler(echo_handler) #detects text
    app.add_handler(test_handler) #detecting invoices

    print("SETTING ERROR HANDLER")
    app.add_error_handler(error)

    print("STARTING POLLING")
    app.run_polling(poll_interval=5)