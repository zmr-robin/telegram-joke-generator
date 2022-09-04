from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
import pyjokes


# telegram api token

updater = Updater("Telegram_Api_Token",use_context=True)

# action that is executed when the bot is started

def start(update: Update, context: CallbackContext):
	update.message.reply_text("Hello if you want to generate english jokes write /en but if you prefer german use /de .")

# memes in the english language
  
def en(update: Update, context: CallbackContext):
  joke = pyjokes.get_joke(language="en", category="neutral")
  update.message.reply_text(joke)

# memes in the german language

def de(update: Update, context: CallbackContext):
  joke = pyjokes.get_joke(language="de", category="neutral")
  update.message.reply_text(joke)

# CommandHandler
  
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('de', de))
updater.dispatcher.add_handler(CommandHandler('en', en))

# start the bot :) 

updater.start_polling()

