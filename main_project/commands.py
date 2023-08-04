from telegram import Update
from telegram.ext import (ContextTypes,
                          CommandHandler)

from env.env import config

BOT_USERNAME = config("BOT_USERNAME", default=None)


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"We live in a society, I am {BOT_USERNAME} btw!"
    )


async def help_command(update, context):
    await update.message.reply_text(f"Working in progress. Did I already tell you we live in a Society?")


async def custom_command(update, context):
    await update.message.reply_text(f"Custom greetings, still in a society")


async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_caps = ''.join(context.args).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)


start_handler = CommandHandler("start", start_command)
help_handler = CommandHandler("help", help_command)
custom_handler = CommandHandler("custom", custom_command)
caps_handler = CommandHandler("caps", caps)