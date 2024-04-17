from telegram import Update 
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from config import TELEGRAM_TOKEN
from telegram_bot.commands import start_command, help_command
from telegram_bot.handlers import handle_text_message, handle_audio, handle_image
from logging_config import *

#Error
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logging.error(f'Update {update} caused error: {context.error}')

#Running
if __name__ == '__main__':
    logging.info('Starting bot...')
    print('Starting bot...')
    # Commands
    app = Application.builder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))

    # Handlers
    app.add_handler(MessageHandler(filters.TEXT, handle_text_message))
    app.add_handler(MessageHandler(filters.VOICE, handle_audio))
    app.add_handler(MessageHandler(filters.PHOTO, handle_image))

    # Errors
    app.add_error_handler(error)

    #Polls the bot
    logging.info('Polling')
    print('Polling')
    app.run_polling(poll_interval=3)