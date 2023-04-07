#!/usr/bin/env python3
import configparser
import os
from telethon import TelegramClient
from colorama import Fore, Back, Style, init
from tqdm import tqdm
import time
import datetime

# Reading Configs
config = configparser.ConfigParser()
config.read("config.ini")
# Setting configuration values
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
api_hash = str(api_hash)
user_username = config['Telegram']['user_username']
bot_username = config['Telegram']['bot_username']

init(autoreset=False)

# Creating the user session
if not os.path.isfile(str(user_username) + ".session"):
    print(Fore.GREEN + "[+] We are creating the session file for user, input your mobile phone number to login (i.e. +57300...)" + Style.RESET_ALL)
client = TelegramClient(user_username, api_id, api_hash)
client.start()
# Creating the bot session
if not os.path.isfile(str(bot_username) + ".session"):
    print(Fore.GREEN + "[+] We are creating the session file for bot, input the bot token (i.e. 4509046619:LMnjdork...)" + Style.RESET_ALL)
bot = TelegramClient(bot_username, api_id, api_hash)
bot.start()

channel = input("Type the scammer channel username (Starts with @ or Telegram URL): ")

async def get_channel_msgs():     
    all_messages = []  
    # Getting the date from last message and deduct 48 hours 
    current_datetime = datetime.datetime.now(datetime.timezone.utc)
    date_minus_48h = current_datetime - datetime.timedelta(hours=48)  

    print(Fore.GREEN + "Phase 1/2 - Getting the last 48 hours of messages" + Style.RESET_ALL)
    msg_count = 0

    # Iterating over channel messages
    async for message in client.iter_messages(channel):
        if message.date > date_minus_48h:
            all_messages.append({"id": message.id, "msg": message.text})
            msg_count += 1             
        else:
            break
        for i in tqdm(range(0, msg_count), desc="Message " + str(msg_count)):            
            time.sleep(.01)
        print("ID " +  Fore.GREEN + str(message.id) + Style.RESET_ALL)         
    print(Fore.GREEN + "Completed! Total messages gathered " + str(len(all_messages)) + Style.RESET_ALL + "\n")       
    return all_messages
    
async def delete_scammer_msgs(list_messages):  
    print(Fore.GREEN + "Phase 2/2 - Deleting the last 48 hours of scammer channel " + channel + Style.RESET_ALL)
    msg_count = 0
    for key in list_messages:        
        try:            
            await bot.delete_messages(channel, key['id'])
            time.sleep(1) # Sleep for 1 second to avoid flooding the servers
            print("[+] Succesfully deleted the message with ID " + Fore.GREEN + str(key['id']) + Style.RESET_ALL)  
            msg_count += 1 
        except Exception as err: 
            pass              
            #To see properly the error, comment the 'pass' and below the error is because of
            #trying to remove id of services messages by Telegram
            #print(Exception, err)  
    print(Fore.GREEN + "Completed! Deleted " + str(msg_count) + " messages from channel." + Style.RESET_ALL + "\n") 

async def send_message_to_scammer():
    while True:
        # Getting your messages to post on the channel
        message = input("Send a final message(s) to the scammer (Type \033[31mCtrl\033[0m to exit): ")        
        if message == 'Ctrl':
            break
        else:
            # Send the message to a specified user or channel
            await bot.send_message(channel, message)

with client:
    channel_msgs = client.loop.run_until_complete(get_channel_msgs())    
with bot:
    bot.loop.run_until_complete(delete_scammer_msgs(channel_msgs))
    bot.loop.run_until_complete(send_message_to_scammer())
