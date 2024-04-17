from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to AudioFaceBot! I'm here to assist you in saving audio messages and detecting faces in photos. When sending audio messages, they will be saved in WAV format with a sampling rate of 16kHz. For photos, I'll only save those that contain faces. Feel free to send me an audio messages or photos, and I'll take care of the rest.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "Sure! Here's how you can use AudioFaceBot:\n\n"
        "• Start: Begin interacting with the bot.\n"
        "• Send Audio Messages: Share audio messages from your dialogues, and they'll be saved in WAV format with a sampling rate of 16kHz.\n"
        "• Send Photos: Share photos, and I'll determine if there are faces present before saving them.\n"
        "• Help: You're here! Get assistance and learn how to use the bot effectively."
    )
    await update.message.reply_text(help_text)    

