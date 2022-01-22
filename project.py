from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import requests

updater = Updater("1066299066:AAHhMYtGCUey7m-w-W1rmd_lt8bRhIfWZKc",use_context=True) #Add your API_TOKEN here 

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello, Welcome to the Bot.Please write /commands to see the available commands")

def commands(update: Update, context: CallbackContext):
	update.message.reply_text("""Available Commands 
	/python - To get the Python download URL
	/github - To get the github URL
	/youtube - To get youtube URL
	/google - To get the Google URL
    /check - To check the BTC price
    /weather - To check the weather of Pune""")


def youtube_url(update: Update, context: CallbackContext):
	update.message.reply_text(
		"https://www.youtube.com")


def python_url(update: Update, context: CallbackContext):
	update.message.reply_text("https://www.python.org/downloads/")


def github_url(update: Update, context: CallbackContext):
	update.message.reply_text("https://www.github.com/")


def google_url(update: Update, context: CallbackContext):
	update.message.reply_text("https://www.google.com")


def unknown(update: Update, context: CallbackContext):
	update.message.reply_text("Sorry '%s' is not a valid command" % update.message.text)


def unknown_text(update: Update, context: CallbackContext):
	update.message.reply_text("Sorry I can't recognize you , you said '%s'" % update.message.text)


def checkprice(update, context):
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    if(response.status_code==200): #The HTTP 200 OK success status response code indicates that the request has succeeded
        data = response.json()
        update.message.reply_text(data)
    else: 
        context.bot.send_message(chat_id=update.effective_chat.id, text="Error, something went wrong.")


def weather_check(update,context):
    response = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Pune,IN&appid=fe44a2c83e558756d342db58661dadd7')
    if(response.status_code==200): #The HTTP 200 OK success status response code indicates that the request has succeeded
        data = response.json()
        update.message.reply_text(data)
    else: 
        context.bot.send_message(chat_id=update.effective_chat.id, text="Error, something went wrong.")


updater.dispatcher.add_handler(CommandHandler('check', checkprice))
updater.dispatcher.add_handler(CommandHandler('weather', weather_check))
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('python', python_url))
updater.dispatcher.add_handler(CommandHandler('commands', commands))
updater.dispatcher.add_handler(CommandHandler('github', github_url))
updater.dispatcher.add_handler(CommandHandler('youtube', youtube_url))
updater.dispatcher.add_handler(CommandHandler('google', google_url))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown)) 
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()
