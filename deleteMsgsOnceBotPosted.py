#!/usr/bin/env python3
import configparser
import os
from telethon import TelegramClient, events, types
from telethon.errors import UnauthorizedError
from colorama import Fore, Style, Back
import datetime

# Reading Configs
config = configparser.ConfigParser()
config.read("config.ini")
# Setting configuration values
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
api_hash = str(api_hash)
bot_username = config['Telegram']['bot_username']

# Creating the bot session
if not os.path.isfile(str(bot_username) + ".session"):
    print(Fore.GREEN + "[+] We are creating the session file for bot, input the bot token (i.e. 4509046619:LMnjdork...)" + Style.RESET_ALL)
bot = TelegramClient(bot_username, api_id, api_hash)
count = 0
print("Listening mode for bot")

#Just deleting the messages once posted on chat(s)/channel(s) associated with this bot
@bot.on(events.NewMessage)
async def my_event_handler(event):    
    chat = await event.get_chat()
    await event.delete()
            
    if isinstance(chat, types.Channel):
        if chat.username is not None:
            print(Back.WHITE + Fore.BLACK + "Message received on chat " + Fore.GREEN + chat.title + 
            Fore.BLACK + ", channel username " + Fore.GREEN + "@" + chat.username + Fore.WHITE +
            Style.RESET_ALL + "\nSucessfully deleted }:)")
        else:
            print(Back.WHITE + Fore.BLACK + "Message received on chat " + Fore.GREEN + str(chat.id) + 
            Style.RESET_ALL + "\nSucessfully deleted }:)")
    elif isinstance(chat, types.User):
        print(Back.WHITE + Fore.BLACK + "Message received on chat " + Fore.GREEN + str(chat.id) +
         Style.RESET_ALL + "\nSucessfully deleted }:)")

    global count
    count += 1
    print(Back.WHITE + Fore.BLACK + "Message catched number " + str(count) + Style.RESET_ALL + "\n")

bot.start()
try:
    bot.run_until_disconnected()    
except UnauthorizedError as e:
    print(Fore.RED + str(e) + "\nToken revoked by scammer at " + str(datetime.datetime.now(datetime.timezone.utc)) + Style.RESET_ALL + "\n")
