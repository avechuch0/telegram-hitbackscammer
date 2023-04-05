#!/usr/bin/env python3
import configparser
import os
from telethon import TelegramClient, types
from colorama import Fore, Back, Style
import sys

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

async def main():
    # Get the channel object    
    entity = input("Type the scammer channel username (Starts with @, Telegram URL or entity ID): ")
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

    channel = await bot.get_entity(channel)

    # Check if User
    if isinstance(channel, types.User):
        print("\n" + Back.WHITE + Fore.RED + "You can't do this because your input belongs to a user entity, not a channel" + Style.RESET_ALL)
        sys.exit(0)
    
    print(Fore.RED + "Are you sure?\nLeaving this channel means a lossing of doing other activities over the channel")
    answer = input("Type 'Yes' to proceed, anything to cancel: " + Style.RESET_ALL)
    if answer == 'Yes':
        try:
            await bot.delete_dialog(channel, revoke = True)
            print("\n" + Fore.GREEN + "Completed! Succesfully leaving the channel " + str(entity) + Style.RESET_ALL)
        except Exception as err:
            print(Exception, err)
            print("It might possible you see you're not a member of channel because you already previously left it")
    elif answer == 'yes':
        print(Fore.RED + "Please type Yes next time once you input the channel again" + Style.RESET_ALL)
        await main()
    elif answer == 'y':
        print(Fore.RED + "Please type Yes next time once you input the channel again" + Style.RESET_ALL)
        await main()
    elif answer == 'Y':
        print(Fore.RED + "Please type Yes next time once you input the channel again" + Style.RESET_ALL)
        await main()    
    else:
        print("\n" + Back.WHITE + Fore.RED + "[-] Not leaving the channel " + str(entity) + " as you cancelled the operation" + Style.RESET_ALL)
            
with bot:
    bot.loop.run_until_complete(main())
