from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# Your bot token from BotFather
TOKEN = "7301448779:AAFzjDhzfjHf-ZhjX6oXMngTBiBn4JAN-2I"

# Define a command handler
def start(update, context):
    keyboard = [[InlineKeyboardButton("Open Link", url="https://gisla.online/app")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Press the button below to open the link:', reply_markup=reply_markup)

# Handle button press
def button(update, context):
    query = update.callback_query
    query.answer()
    # Here you can handle any other actions when the button is pressed

def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add command handler for /start
    dp.add_handler(CommandHandler("start", start))

    # Add callback query handler for button presses
    dp.add_handler(CallbackQueryHandler(button))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()
