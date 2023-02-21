#!/usr/bin/env python3
import configparser
from telethon import TelegramClient, types
from colorama import Fore, Back, Style, init

# Reading Configs
config = configparser.ConfigParser()
config.read("config.ini")
# Setting configuration values
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
api_hash = str(api_hash)
bot_username = config['Telegram']['bot_username']

# Creating the bot session
print(Fore.GREEN + "[+] We are creating the session file for bot, input the bot token (i.e. 4509046619:LMnjdork...)" + Style.RESET_ALL)
bot = TelegramClient(bot_username, api_id, api_hash)
bot.start()

async def check_scammer_channel():
    entity = input("Type the scammer channel : ")
    if entity.isnumeric():
        channel = int(entity)  
    # Negative numbers  
    elif entity[0] == '-':
        if entity[1:].isnumeric():
            channel = -abs(int(entity))          
        else:
            channel = entity                    
    else:
        channel = entity

    try:
        channel = await bot.get_entity(channel)
        if isinstance(channel, types.Channel):            
            if channel.username is None:
                print(Fore.GREEN + 'The channel is private.' + Style.RESET_ALL)                
            else: 
                print(Fore.GREEN + 'The channel is public.' + Style.RESET_ALL)
        elif isinstance(channel, types.User):
            print(Fore.GREEN + 'This entity is not properly a channel, it belongs to a user account.\nBut no worries, you can treat this as a private channel' + Style.RESET_ALL) 
    except Exception as err:
        print(Fore.RED + "The username you provided seems not existing on Telegram ecosystem." + Style.RESET_ALL)          
        
with bot:
    bot.loop.run_until_complete(check_scammer_channel())
