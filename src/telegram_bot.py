from telegram.ext import Updater, CommandHandler

import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bot started!")

def stop(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bot stopped!")
    updater.stop()

def sleep(update, context):
    try:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Computer set to sleep")
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    except:
        context.bot.send_message(chat_id=update.effective_chat.id, text="There was an error executing rundll32.exe")

updater = Updater(token='1444445693:AAE3kt0xQI8fI1leICf3tU64cSCNLaxJEpw', use_context=True)
dispatcher = updater.dispatcher

start_handler = CommandHandler("start", start)
stop_handler = CommandHandler("stop", stop)
sleep_handler = CommandHandler("sleep", sleep)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(stop_handler)
dispatcher.add_handler(sleep_handler)

updater.start_polling()

