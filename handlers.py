from env import config
from telegram import Update
from telegram.ext import (MessageHandler, 
                          filters, 
                          ContextTypes,
                          MessageHandler)

BOT_USERNAME = config("BOT_USERNAME", default=None)

def handle_response(text):
    cleaned_text = text.lower()
    if "society" in cleaned_text:
        return "We live in a society"
    else:
        return "I didn't percieve any society in your message. I lost interest"


async def handle_message(update, context):
    message_type = update.message.chat.type #Group or private chat
    text = update.message.text
    print(f"User {update.message.chat.id} sent this in {message_type}: {text}")

    if message_type == "group":
        if BOT_USERNAME in text:
            new_text = text.replace(BOT_USERNAME, "").strip()
            response = handle_response(new_text)
        else:
            return
    else:
        response = handle_response(text)
    print("Bot says:", response)
    await update.message.reply_text(response)

async def error(update, context):
    print(f"Update {update} caused error {context.error}")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

async def test(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("AUDIO RECIEVED")
    new_file = await context.bot.get_file(update.message.voice.file_id)
    download_file = await new_file.download_to_drive(f"media/voice_note.ogg")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="got some audio")


msg_handler = MessageHandler(filters.TEXT, handle_message)
test_handler = MessageHandler(filters.VOICE, test)
echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)