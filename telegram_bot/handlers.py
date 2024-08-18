from telegram import Update
from telegram.ext import MessageHandler, filters, ContextTypes
from telegram_bot.responses import generate_text
from telegram_bot.downloads import download_audio, download_image
from audio_processing import process_audio
from image_processing import process_image
from dbconnection import store_audio, store_image
import logging

async def handle_text_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text: str = update.message.text
    response: str = generate_text(text, update)

    await update.message.reply_text(response)

async def handle_audio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        audio = await download_audio(update)
        processed_audio = await process_audio(audio)
        store_audio_db = store_audio(update.effective_user.id,processed_audio)
        await update.message.reply_text('Audio converted to wav and stored in our database.')
    except Exception as e:
        logging.error(f'Error at handle audio: {str(e)}')
        await update.message.reply_text(f'Sorry, an error occurred. Please try again later.')

async def handle_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        await update.message.reply_text("Thank you for sending the image. Processing may take a few seconds.")

        image = await download_image(update)
        processed_image = await process_image(image)

        if processed_image: 
            store_image_db = store_image(update.effective_user.id,processed_image) 
            await update.message.reply_text("There is at least one face in this image, so I will store it in our database.")
        else:
            await update.message.reply_text("There is not one face in this image, so I won't store it in our database.")

    except Exception as e:
        logging.error(f'Error at handle image: {str(e)}')
        await update.message.reply_text(f'Sorry, an error occurred. Please try again later.')
             


             
