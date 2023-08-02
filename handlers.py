from env import config

BOT_USERNAME = config("BOT_USERNAME", default=None)

def handle_response(text):
    cleaned_text = text.lower()
    if "society" in cleaned_text:
        return "We live in a society"
    else:
        return "I didn't percieve any society in your message. I lost interest"
    return "tf you wrote this is out of the possible options"

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