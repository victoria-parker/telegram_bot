from telegram import Update


def generate_text(text: str, update:Update) -> str:
    processed: str = update.message.text.lower()

    if 'hello' or 'hi' or 'hey' in processed:
        return f'Hello {update.effective_user.first_name}'

    return ' I generally do not talk much, I mainly process audio messages and detect faces in pictures. Send me an audio message or a picture and I will be happy'