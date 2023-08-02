from env import config

BOT_USERNAME = config("BOT_USERNAME", default=None)

async def start_command(update, context):
    await update.message.reply_text(f"We live in a society, I am {BOT_USERNAME} btw")

async def help_command(update, context):
    await update.message.reply_text(f"Working in progress. Did I already tell you we live in a Society?")

async def custom_command(update, context):
    await update.message.reply_text(f"Custom greetings, still in a society")
