import requests

from telegram import Update
from telegram.ext import (MessageHandler, 
                          filters, 
                          ContextTypes,
                          MessageHandler)

from env.env import config
from utils.convert_audio import convert_audio
from main_project.settings import config as files_config


MEDIA_FOLDER = files_config["MEDIA_FOLDER"]
API_BASE_URL = files_config["API_BASE_URL"]
BOT_USERNAME = config("BOT_USERNAME", default=None)


def handle_response(text):
    cleaned_text = text.lower()
    if "society" in cleaned_text:
        return "We live in a society"
    else:
        return "I didn't percieve any society in your message. I lost interest"


async def handle_message(update, context):
    """
    Handles messages sent by users depending on the chat type
    """
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
    """
    Error msg if something weird happens
    """
    print(f"Update {update} caused error {context.error}")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Echo function, returns the text gotten from the user
    """
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


async def audio_to_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Transcribes the audio sent by the user using local Whisper server
    The user sends and audio file, the bot downloads it, 
    converts it to mp3, sends it to the server
    """
    await update.message.reply_text("Starting transcription")
    url_files = f"{API_BASE_URL}/transcribe"
    print("AUDIO RECIEVED")

    new_file = await context.bot.get_file(update.message.voice.file_id)
    await new_file.download_to_drive(f"{MEDIA_FOLDER}voice_note.ogg")
    print("AUDIO DOWNLOADED")

    convert_audio("voice_note.ogg", "ogg", "mp3")
    print("AUDIO CONVERTED")

    with open(f"{MEDIA_FOLDER}voice_note.mp3", 'rb') as fd:
        content = fd.read()

    context = {"file" : content}
    print("STARTING TRANSCRIPTION")

    response = requests.post(url_files, files=context)
    print("TRANSCRIPTION DONE")

    transcript = response.json()["transcription"]

    print(f"MESSAGE: {transcript}")

    await update.message.reply_text(transcript)    
    await update.message.reply_text("Transcription done")    
    #await context.bot.send_audio(chat_id=update.effective_chat.id, audio=open("media/voice_note.mp3", "rb"))


msg_handler = MessageHandler(filters.TEXT, handle_message)
audio_to_text_handler = MessageHandler(filters.VOICE, audio_to_text)
echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)