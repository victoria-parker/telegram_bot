from telegram import Update
from telegram.ext import MessageHandler, filters, ContextTypes
from telegram_bot.responses import handle_response

async def handle_text_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text: str = update.message.text
    response: str = handle_response(text, update)

    await update.message.reply_text(response)