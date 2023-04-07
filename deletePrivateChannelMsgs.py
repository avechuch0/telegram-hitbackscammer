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
bot_username = config['Telegram']['bot_username']

init(autoreset=False)

# Creating the bot session
if not os.path.isfile(str(bot_username) + ".session"):
    print(Fore.GREEN + "[+] We are creating the session file for bot, input the bot token (i.e. 4509046619:LMnjdork...)" + Style.RESET_ALL)
bot = TelegramClient(bot_username, api_id, api_hash)
bot.start()

async def get_scammer_channel():
    entity = input("Type the scammer channel, (It is a numeric value): ")
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
    return channel

async def get_channel_msgs(channel):        
    all_messages = []   
    # Getting the date from last message and deduct 48 hours
    last_msg = await bot.send_message(channel, "...")    
    date_minus_48h = last_msg.date - datetime.timedelta(hours=48)

    print(Fore.GREEN + "Phase 1/2 - Getting the last 48 hours of messages" + Style.RESET_ALL)
    msg_count = 0

    # Iterating over channel messages 
    msg_id = int(last_msg.id)    
    while msg_id >= 0:
        try:
            message = await bot.get_messages(channel, ids=msg_id)       
            if message.date > date_minus_48h:
                none_count = 0
                all_messages.append({"id": message.id, "msg": message.text})
                msg_count += 1
                msg_id -= 1    
                for i in tqdm(range(0, msg_count), desc="Message " + str(msg_count)):            
                    time.sleep(.01)  
                print("ID " +  Fore.GREEN + str(message.id) + Style.RESET_ALL)                         
            else:
                break         
        #Handling NoneType data
        except Exception as err: 
            none_count += 1
            msg_id -= 1
            if none_count >= 30:
                break

    print(Fore.GREEN + "Completed! Total messages gathered " + str(msg_count) + Style.RESET_ALL + "\n")    
    return all_messages 

async def delete_scammer_msgs(channel, list_messages): 
    print(Fore.GREEN + "Phase 2/2 - Deleting the last 48 hours of scammer channel " + str(channel) + Style.RESET_ALL)
    msg_count = 0
    for key in list_messages:        
        try:            
            await bot.delete_messages(channel, key['id'], revoke=True)
            time.sleep(1) # Sleep for 1 second to avoid flooding the servers
            print("[+] Succesfully deleted the message ID " + Fore.GREEN + str(key['id']) + Style.RESET_ALL)  
            msg_count += 1
        except Exception as err: 
            pass              
            #To see properly the error, comment the 'pass' and below the error is because of
            #trying to remove id of services messages by Telegram
            #print(Exception, err)  
    print(Fore.GREEN + "Completed! Deleted " + str(msg_count) + " messages from channel." + Style.RESET_ALL + "\n")    

async def send_message_to_scammer(channel):
    while True:
        # Getting your messages to post on the channel
        message = input("Send a final message(s) to the scammer (Type \033[31mCtrl\033[0m to exit): ")        
        if message == 'Ctrl':
            break
        else:
            # Send the message to a specified user or channel
            await bot.send_message(channel, message)

with bot:
    channel = bot.loop.run_until_complete(get_scammer_channel())
    channel_msgs = bot.loop.run_until_complete(get_channel_msgs(channel))  
    bot.loop.run_until_complete(delete_scammer_msgs(channel, channel_msgs))
    bot.loop.run_until_complete(send_message_to_scammer(channel))
