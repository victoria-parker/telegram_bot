from telegram import Update


def generate_text(text: str, update:Update) -> str:
    processed: str = update.message.text.lower()

    if 'hello' in processed or 'hi' in processed or 'hey' in processed:
        return f'Hello {update.effective_user.first_name}'

    return 'Hey there! While I may not chat much, I excel at processing audio messages and detecting faces in pictures. Feel free to send me an audio message or a picture, and I\'ll be more than happy to assist you!'