from telegram import Update
from telegram.ext import MessageHandler, filters, ContextTypes
from telegram_bot.responses import generate_text
from telegram_bot.downloads import download_audio, download_image
from audio_processing import process_audio
from dbconnection import store_audio

async def handle_text_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text: str = update.message.text
    response: str = generate_text(text, update)

    await update.message.reply_text(response)

async def handle_audio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        audio = await download_audio(update)
        processed_audio = await process_audio(audio)
        store_audio_db = store_audio(update.effective_user.id,processed_audio)
        await update.message.reply_text('audio converted to wav and stored in our database')
    except Exception as e:
        await update.message.reply_text(f'Sorry, an error occurred: {str(e)}')

async def handle_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
        try:
            image = await download_image(update)
            await update.message.reply_text('img temporarely downloaded')
        except Exception as e:
            await update.message.reply_text(f'Sorry, an error occurred: {str(e)}')