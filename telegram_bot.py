import time
import os
import telepot
from telepot.loop import MessageLoop
from telegram import ParseMode
from message import *
#from database import Identificationnumber, email
from app import User, Regester

HTTP_API = os.environ['HTTP_API']


form = Regester()
Identificationnumber = User.query.filter_by(ID=form.ID.data)
email = User.query.filter_by(email=form.email.data)
      

def handle(msg):
    
    chat_id = msg['chat']['id']
    command = msg['text']
    print(command)

    if command == '/start':
        bot.sendMessage(chat_id, message_1)
    elif command == f'{Identificationnumber}':
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



