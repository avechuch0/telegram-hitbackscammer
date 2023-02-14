#!/usr/bin/env python3
import configparser
from telethon import TelegramClient, events, types
from colorama import Fore, Style, Back

# Reading Configs
config = configparser.ConfigParser()
config.read("config.ini")
# Setting configuration values
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
api_hash = str(api_hash)
bot_username = config['Telegram']['bot_username']

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
bot.run_until_disconnected()