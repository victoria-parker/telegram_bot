from telegram.ext import Application, CommandHandler, MessageHandler, filters
from config import TELEGRAM_TOKEN
from telegram_bot.commands import start_command, help_command
from telegram_bot.handlers import handle_text_message, handle_audio

#Running
if __name__ == '__main__':
    print('Starting bot...')
    # Commands
    app = Application.builder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))

    # Responses
    app.add_handler(MessageHandler(filters.TEXT, handle_text_message))
    app.add_handler(MessageHandler(filters.VOICE, handle_audio))

    #Polls the bot
    print('Polling')
    app.run_polling(poll_interval=3)