from telegram.ext import (
    Application, 
    CommandHandler, 
    MessageHandler, 
    filters)

from env import config
from commands import start_command, help_command, custom_command
from handlers import handle_message, error

API_TOKEN = config("API_TOKEN", default=None)
BOT_USERNAME = config("BOT_USERNAME", default=None)
BOT_NAME=config("BOT_NAME", default=None)


if __name__ == '__main__':
    print("BUILDING APP")
    app = Application.builder().token(API_TOKEN).build()

    print("SETTING COMMANDS")
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("custom", custom_command))

    print("SETTING MSG HANDLER")
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    print("SETTING ERROR HANDLER")
    app.add_error_handler(error)

    print("STARTING POLLING")
    app.run_polling(poll_interval=5)