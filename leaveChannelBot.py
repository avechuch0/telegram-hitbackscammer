#!/usr/bin/env python3
import configparser
from telethon import TelegramClient, types
from colorama import Fore, Style
import sys

# Reading Configs
config = configparser.ConfigParser()
config.read("config.ini")
# Setting configuration values
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
api_hash = str(api_hash)
bot_username = config['Telegram']['bot_username']

# Creating the 'bot' session with bot_username string
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
        print(Fore.RED + "You can't do this action in private chats")
        sys.exit(0)
    
    print(Fore.RED + "Are you sure?\n" + Fore.WHITE + "Leaving this channel means a lossing of doing other activities over the channel")
    answer = input("Type 'Yes' to proceed, anything to cancel: ")
    if answer == 'Yes':
        try:
            await bot.delete_dialog(channel, revoke = True)
            print(Fore.GREEN + "Succesfully leaving the channel " + str(entity) + Style.RESET_ALL)
        except Exception as err:
            print(Exception, err)
            print("It might possible you see you're not a member of channel because you already previously left it")
    elif answer == 'yes':
        print("Please type Yes next time")
        await main()
    elif answer == 'y':
        print("Please type Yes next time")
        await main()
    elif answer == 'Y':
        print("Please type Yes next time")
        await main()    
    else:
        print("Not leaving the channel " + str(entity) + " as you cancelled the operation")
            
with bot:
    bot.loop.run_until_complete(main())
