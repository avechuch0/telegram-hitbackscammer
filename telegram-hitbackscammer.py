#!/usr/bin/env python3
import configparser
import subprocess
import os
import sys
from telethon import TelegramClient
from colorama import Fore, Back, Style
from colorama import init

AUTHOR = "Jaime Bello"
VERSION = "1.0 February 2023"

'''
Install dependencies with:
pip install -r requirements.txt
pip3 install -r requirements.txt
'''

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

header = r'''
 _____    _                                                      :~?YPGGBBBBBBGGPY?~:               
|_   _|  | |                                                 .!YGB#&&@@@@@@@@@@&&&#GY!.           
  | | ___| | ___  __ _ _ __ __ _ _ __ ___                  ~5B#&&@@@@@@@@@@@@@@@@@@@&#B5~         
  | |/ _ \ |/ _ \/ _` | '__/ _` | '_ ` _ \               !PB#&@@@@@@@@@@@@@@@@@@@@@@@@@@&&BP!       
  | |  __/ |  __/ (_| | | | (_| | | | | | |            ^PB#&&&&@@@@@@@@@@@@@@@@@@@@@@@@&&&&#BP^     
  \_/\___|_|\___|\__, |_|  \__,_|_| |_| |_|           7GB#&&&&&&&@@@@@@@@@@@@@@@@@@@&&&&&&&&#BG7    
                  __/ |                              ?BBB&&&&&&&&&&&&&@@@@@@@@BPGPB&&&&&&&&&&#BB7   
  _   _ _ _     |___/_                _             ~GBB#&&&&&&&&&&&&&&&&@@@@5     Y@&&&&&&&&#BBG~  
 | | | (_) |        | |              | |           .PBBB##&&&&&##&&&&&&&&&&&&P     P&&&&&&&&##BBBP. 
 | |_| |_| |_  ____ | |__   __ _  ___| | __        ~GBBB###&5     Y&&&&&&&&&&&     &&&&&&&&###BBBG~ 
 |  _  | | __| ____ | '_ \ / _` |/ __| |/ /        7GGBBB##&P     P&&&&&&&&&&&&&&&&&&&&&&&###BBBGG7 
 | | | | | |_       | |_) | (_| | (__|   <         7GGBBB###&     &&&&&&&&&&&&&&&&&&% #&&####BBBGG7 
 \_| |_/_|\__|      |_.__/ \__,_|\___|_|\_\        ~PGGBBBB##&###&&&&&&&&&&&&&&&&&%   #&###BBBBGGP~ 
 ___  ___ __ _ _ __ ___  _ __ ___   ___ _ __       .5PGGGBBB####&&&&&&&&&&&&&&P    .G&###BBBGGGPP   
/ __|/ __/ _` | '_ ` _ \| '_ ` _ \ / _ \ '__|     :5GGPPP&&&&&&&&&&&&&&&&&PP     .5#BBBGGGGGPGG:    
\__ \ (_| (_| | | | | | | | | | | |  __/ |         :^7&&&&&&&&&&&&&PPP         .GGGGPPPPPPPPP:.     
|___/\___\__,_|_| |_| |_|_| |_| |_|\___|_|          !55PGGGGGGGGGGGG         ###5Y?JGGGGGGGGG5~.    
                                                       .5##BBBBB######      ########5PB#BBBBBBB     
                                                   .!YPB#&&&&&&&&&&&&&&&   &&&&&&&&&&&&&&&&&&#Y     
                                                  .B&&@@@@&&&BPY7!^^:::^~7 #&&&&&@@@@@&&&           
                                                   7PGGG5J!:.                ..:^~~!!~~^:.          '''

                                                                     
header2 = r'''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠤⠖⠒⠉⠉⠁⠀⠀⠀⠀⠀⠉⠉⠁⠒⠢⠄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠴⠊⠁⠀⢀⣠⠤⠒⠒⠋⠉⠉⠉⠉⠉⠑⠒⠒⠤⣀⡀⠀⠉⠒⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠊⠀⢀⡠⠖⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠢⡀⠁⠑⢤⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⡴⠉⠀⣠⠔⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠢⡀⠘⠳⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡰⠋⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣄⠀⠘⣆⠀⠀⠀⠀
⠀⠀⠀⠀⢀⡜⠁⠀⡴⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢆⠀⠈⣆⠀⠀⠀
⠀⠀⠀⠀⡞⠀⠀⡜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣟⡽⣿⣿⡧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣆⠀⢿⡄⠀⠀
⠀⠀⢰⠇⠀⢸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣷⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡄⠘⣷⠀⠀
⠀⠀⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⣄⡄⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⢹⡇⠀
⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡿⢿⣿⢿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡇⠀
⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⣟⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀
⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣟⣯⣷⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀
⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⢿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡇⠀
⠀⠀⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢙⠿⣿⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠤⠤⠤⠚⣉⡆
⣇⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠭⣛⠻⠿⢿⣿⣶⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠷⣶⣶⠶⠽⠟⠁
⠙⣧⣄⡑⠂⠤⠤⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠙⠛⠻⢶⣦⣤⡀⠀⠀⠀⢀⣀⠀⠉⠳⡄⠀⠀
⠀⠈⠙⠻⠷⠶⣶⣦⣌⣳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣤⡤⠤⠤⠤⠶⠶⠿⠛⠃⠀⠀⢰⣧⣤⣤⣶⠿⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠿⠶⠶⠶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣄⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣀⡤⠞⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠤⢀⠀
⠀⠀⠀⠀⠀⢰⣃⠐⠦⠤⠤⠄⠀⠠⠤⠤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣵
⠀⠀⠀⠀⠀⠀⠛⠿⠶⠦⠶⠶⠶⠶⢶⣂⡤⣤⡉⠉⠀⠐⠒⠒⠒⠒⠒⠒⠒⠒⠀⠀⠉⠉⢉⣀⠀⡉⠉⠉⠀⠐⠒⠤⠤⠀⠀⠄⢀⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⠛⠛⠛⠳⠶⠶⠶⠶⠶⠶⠿⠚⠚⠛⠓⠀⠀⠀⠀⠈⠛⠛⠓⠶⣶⣶⣤⣤⣶⡾⠋
'''

foreground = True

def menu():
    print(Style.RESET_ALL)
    #Just the logo on the first time
    if foreground is True:
        print(Fore.WHITE + Back.BLUE)
        # Fixing the logo to print it justified
        for line in header.split('\n'):            
            print(f"{line:<120}")
        
        yellow_banner = "  Use the scammers' bot to screw up their activities"
        print(Fore.BLACK + Back.YELLOW + f"{yellow_banner:^120}") 
        print(Fore.BLACK + Back.YELLOW + f"{AUTHOR + ' - ' + VERSION:^120}")  
        print(Style.RESET_ALL + "\n")
    print("".rjust(2) + "Please select an option:")
    print("".rjust(2) + "1. Doubts? - Check if the channel is public or private")
    print("".rjust(2) + "2. Get the list of channel administrators")
    print("".rjust(2) + "3. Delete the last 48 hours messages of a public channel  - (Only for public channels)")
    print("".rjust(2) + "4. Delete the last 48 hours messages of a private channel - (Only for private channels)")
    print("".rjust(2) + "5. Listening mode for bot to delete any incoming messages")
    print("".rjust(2) + "6. Leave the channel - (Available for both Public/Private channels)")
    print("".rjust(2) + "7. Exit\n")
    choice = input("".rjust(2) + "Enter your choice: ")
    
    return choice

login = True
def check_config():
    if not api_id or not api_hash or not user_username or not bot_username:
        print("".ljust(2) + ":( \n  Please check the config.ini file and fill the variables to use this program, any there can be empty")        
        return False    
    else:
        global login
        if login is True:        
            # Creating the 'user' session
            if not os.path.isfile(str(user_username) + ".session"):
                print(Fore.GREEN + "[+] We are creating the session file for user, input your mobile phone number to login (i.e. +57300...)" + Style.RESET_ALL)                    
            client = TelegramClient(user_username, api_id, api_hash)
            client.start()
            client.disconnect()
            # Creating the 'bot' session
            if not os.path.isfile(str(bot_username) + ".session"):
                print(Fore.GREEN + "[+] We are creating the session file for bot, input the bot token (i.e. 4509046619:LMnjdork...)" + Style.RESET_ALL)
            bot = TelegramClient(bot_username, api_id, api_hash)
            bot.start()
            bot.disconnect()            
            login = False
        return True

while check_config():    
    choice = menu()
    if sys.platform.startswith('win'):
        if choice == "1":        
            subprocess.run(["python", "checkChannel.py"], check=True)        
            foreground = False
        elif choice == "2":        
            subprocess.run(["python", "getChannelAdmins.py"], check=True)        
            foreground = False
        elif choice == "3":
            subprocess.run(["python", "deleteChannelMsgs.py"], check=True)
            foreground = False
        elif choice == "4":
            subprocess.run(["python", "deletePrivateChannelMsgs.py"], check=True)
            foreground = False
        elif choice == "5":
            subprocess.run(["python", "deleteMsgsOnceBotPosted.py"], check=True)
            foreground = False
        elif choice == "6":
            subprocess.run(["python", "leaveChannelBot.py"], check=True)
            foreground = False
        elif choice == "7":
            break
        else:
            foreground = False
            for line in header2.split('\n'):            
                print(f"{line:<120}")
            
            print(Fore.BLACK + Back.WHITE)
            print(header2.ljust(120))
            print("".rjust(2) + "Invalid choice. Please try again.")
            print(Style.RESET_ALL)

    elif sys.platform.startswith('linux'):
        if choice == "1":        
            subprocess.run(["python3", "checkChannel.py"], check=True)        
            foreground = False
        elif choice == "2":        
            subprocess.run(["python3", "getChannelAdmins.py"], check=True)        
            foreground = False
        elif choice == "3":
            subprocess.run(["python3", "deleteChannelMsgs.py"], check=True)
            foreground = False
        elif choice == "4":
            subprocess.run(["python3", "deletePrivateChannelMsgs.py"], check=True)
            foreground = False
        elif choice == "5":
            subprocess.run(["python3", "deleteMsgsOnceBotPosted.py"], check=True)
            foreground = False
        elif choice == "6":
            subprocess.run(["python3", "leaveChannelBot.py"], check=True)
            foreground = False
        elif choice == "7":
            break
        else:
            foreground = False
            for line in header2.split('\n'):            
                print(f"{line:<120}")
            
            print(Fore.BLACK + Back.WHITE)
            print(header2.ljust(120))
            print("".rjust(2) + "Invalid choice. Please try again.")
            print(Style.RESET_ALL)