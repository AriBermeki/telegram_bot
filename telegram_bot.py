import time
import os
import telepot
from telepot.loop import MessageLoop
from telegram import ParseMode
from message import *
from database import email, Identificationnumber
HTTP_API = os.environ['HTTP_API']

#HTTP_API = Bot_Tocken

id = Identificationnumber
email = email
def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print(command)

    if command == '/start':
        bot.sendMessage(chat_id, message_1)
    elif command == f'{id}':
        bot.sendMessage(chat_id, message_2)
        time.sleep(5)
        bot.sendMessage(chat_id, message_3)

    elif command == f'{email}':
        time.sleep(5)
        bot.sendMessage(chat_id, message_4)
        time.sleep(1)
        bot.sendMessage(chat_id, message_5, parse_mode= ParseMode.HTML)
        
    else:
        bot.sendMessage(chat_id, message_error)

bot = telepot.Bot(HTTP_API)

MessageLoop(bot, handle).run_as_thread()
print ('I am listening ...')

while 1:
    time.sleep(10)


