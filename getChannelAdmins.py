#!/usr/bin/env python3
import configparser
import sys
import os
from telethon import TelegramClient, types
from tabulate import tabulate
from colorama import Fore, Style, init
import time

# Reading Configs
config = configparser.ConfigParser()
config.read("config.ini")
# Setting configuration values
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
api_hash = str(api_hash)
bot_username = config['Telegram']['bot_username']

init(autoreset=False)

# Creating the 'bot' session
if not os.path.isfile(str(bot_username) + ".session"):
    print(Fore.GREEN + "[+] We are creating the session file for bot, input the bot token (i.e. 4509046619:LMnjdork...)" + Style.RESET_ALL)
bot = TelegramClient(bot_username, api_id, api_hash)

async def main():
    # Get the channel object
    entity = input("Please type the scammer channel username (Starts with @, Telegram URL or entity ID: ")
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

    # Check if User
    if isinstance(await bot.get_entity(channel), types.User):
        print(Fore.RED + "This entity belongs to a user, not a channel. That's why it is not possible to get the list of administrators")
        sys.exit(0)

    # Get the administrators of the channel    
    admins = await bot.get_participants(channel, filter=types.ChannelParticipantsAdmins())
    
    table_admins = []
    first_row = ['id', 'is_bot', 'username', 'first_name', 'last_name', 'phone', 'is_creator']
    table_admins.append(first_row) # First row of the table
     
    for admin in admins:
        admin_id = str(admin.id)
        is_bot = str(admin.bot)
        if admin.username is not None:
            username = str(admin.username)
        else:
            username = "None"
        if admin.first_name is not None:
            first_name = str(admin.first_name)
        else:
            first_name = "None"
        if admin.last_name is not None:
            last_name = str(admin.last_name)
        else:
            last_name = "None"
        ''' 
        Please, take into account with bot session
        you cannot retrieve the phone information, you 
        need to be logged with an user account 
        '''        
        if admin.phone is not None:
            phone = str(admin.phone)
        else:
            phone = "None"
        
        try:
            permissions = await bot.get_permissions(channel, admin.id)
            if permissions.is_creator is True: 
                table_admins.append([('\033[31m' + admin_id), is_bot, username, first_name, last_name, phone, (str(permissions.is_creator) + '\033[0m')])            
            else:
                table_admins.append([admin_id, is_bot, username, first_name, last_name, phone, str(permissions.is_creator)])
        except Exception as err:
            print(Fore.RED + "Unfortunately, this bot don't have permissions to get the list of channel administrators" + Style.RESET_ALL)
            sys.exit(0)

    print("\nThe following are the administrators of the channel " + str(entity) + ":")
    print(tabulate(table_admins, headers='firstrow', tablefmt='pretty'))
    await analysis_notes(channel)

async def analysis_notes(channel):
    bot_permissions = await bot.get_permissions(channel, 'me')
    print("Well, our dear scammer must be the owner of the channel in" + Fore.RED + " red row" + Fore.WHITE + ", not the bot itself.")
    print("Although bots can be channel owners, it's not very often seen.\n")
    if bot_permissions.add_admins is True:
        print(Fore.GREEN + "Fortunately!!!" + Fore.WHITE + " this bot to post stolen data of victims" +
        Fore.GREEN + " has the permissions to add admins" + Fore.WHITE + ",")        
        print("you can add a user admin to see properly the whole data of administrators and channel owner,")
        print("including their phone number. A bot can't retrieve some information such as phone number")
        print("it due it's how the nature of bots where designed by Telegram like that...") 
        print("And it's a security feature :)")
        print("Only normal admin users on channels can retrieve information such as the phone number.\n")
    else:
        print(Fore.RED + "Unfortunately :( " + Fore.WHITE + "this scammer is kind of clever and " + Fore.RED + 
        "we cannot add administrators to the channel ")        
        print("" + Fore.WHITE + "using this bot in order to try getting further information of our scammer, ")
        print("such as their phone number.")
        print("A bot can't retrieve some information such as phone number it due it's how the nature of") 
        print("bots where designed by Telegram like that... And it's a security feature :)")
        print("Only normal admin users on channels can retrieve information such as the phone number.\n")
    time.sleep(7)
    
with bot:
    bot.loop.run_until_complete(main())
