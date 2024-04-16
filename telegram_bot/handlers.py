from telegram import Update
from telegram.ext import MessageHandler, filters, ContextTypes
from telegram_bot.responses import generate_text
from telegram_bot.downloads import download_audio
from audio_processing import process_audio

async def handle_text_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text: str = update.message.text
    response: str = generate_text(text, update)

    await update.message.reply_text(response)

async def handle_audio(update: Update, context: ContextTypes.DEFAULT_TYPE):

    audio = await download_audio(update)
    processed_audio = await process_audio(audio)
    # store_audio_db = await save_audio(processed_audio)

    await update.message.reply_text('audio convertido y guardado en nuestra base de datos')