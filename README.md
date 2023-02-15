[![Actively Maintained](https://img.shields.io/badge/Maintenance%20Level-Actively%20Maintained-green.svg)](https://gist.github.com/cheerfulstoic/d107229326a01ff0f333a1d3476e068d)

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/avechuch0)

# Telegram-hitbackscammer 
This is a set of scripts and protocols to do some active defense and offensive countermeausures against scammers/phishers who use Telegram chats/channels as part of phishing kits.

telegram-hitbackscammer.py is a practical application of Annoyance, Attribution and Attack core concepts of active defense and offensive countermeausures to screw up threat actor activities, which can help with combating data theft, financial fraud prevention, impersonation, save people's data, and contributing for a world free of phishing :)

Want more information around these concepts? Take a look of this:

* https://icdt.osu.edu/offensive-countermeasures-art-active-defense </br>
* https://en.wikipedia.org/wiki/Active_defense </br>
* https://www.sans.org/white-papers/36240/ </br>
* https://www.slideshare.net/JaimeAndrsBelloVieda/una-mirada-a-la-active-defense-harbinger-distribution-como-herramienta-de-monitoreo-y-defensa-activa-ante-ataques </br>

# Why it has been developed?
The goal of this development is to help security researchers, threat hunters, incident responders, individuals and even the affected companies with the provision of a protocol to be more proactive in terms of defending against phishing attacks where Telegram is used to store the stolen data.

Attackers on the wild are using Telegram as infrastructure to store the data once a victim fall into the trap. The options vary between public/private channels and private chats.

# Quick Overview
Default mode - Running *telegram-hitbackscamer.py*

![pic](https://github.com/avechuch0/telegram-hitbackscammer/blob/main/images/main.png)

# Options Description
### 1. Doubts? - Check if the channel is public or private
If you don't know whether the channel found on the phishing kit is public or private, use this option to check it. </br>
More info about the Telegram chats/channels: https://telegram.org/faq_channels

### 2. Get the list of administrators for channel
Get a list of scammer channel`s administrators, then you may see who is the owner of the channel and make a threat attribution, i.e. identify the responsible scammer/phisher.

### 3. Delete the last 48 hours messages of public channel  - (Only for public channels)
Selecting this option, you can read and delete up to the last 48 hours of messages of **public** scammer channel. **Be sure to input a public channel once you are asked if you want to avoid errors.**

### 4. Delete the last 48 hours messages of private channel - (Only for private channels)
Selecting this option, you can read and delete up to the last 48 hours of messages of **private** scammer channel. **Be sure to input a private channel once you are asked if you want to avoid errors.**

### 5. Listening mode for bot to delete any incoming messages
This is an interesting option if you want to annoy the scammer a lot!

This option has the power to inmediately delete any try posting message the scammer bot would like to store on channel/chat. No matter what channel/chat id you already found on the phishing, this has the plus of **deleting inmediately the messages for any post in any channel/chat the scammer has set up.**

Once you select this option you will see the message "Listening mode for bot", and any time a victim inputs data on a phishing associated with the bot-token value, you would be notified on the shell with a successfully message deletion, while the scammer would be fucked up and unable to see what the bot tried to post.

### 6. Leave the channel - (Available for both Public/Private channels)
This simply unattach/leave the scammer channel where the bot is linked. This is a silent annoying way to avoid further posting for bot on the channel, but has 2 disadvantages.
1. The scammer/phisher would not be notified about this action, but once he/she checks the list of administrators, they would realize what happened, it's up to them include again the bot or not.
2. **And the most important disadvantage:** </br> 
Once you leave a channel, you won't be able to do anything else on the channel. **This should be your last option/decision due the lack of control once you leave.**

### 7. Exit
Just to finish the program.

# Getting started
1. Download / clone the repo
2. Install required packages: pip3 install -r requirements.txt
3. Get the Telegram API keys (api_id and api_hash) following the instructions here https://core.telegram.org/api/obtaining_api_id
4. Set the API keys in your config.ini file
5. You're ready to go :) simply run the main script *python .\telegram-hitbackscammer.py* or *python3 .\telegram-hitbackscammer.py* depending how you are calling your python instance
6. The first time, you would be asked for a kind of login, **input first your mobile number** including the +, then you would be asked for the bot-token, which would be the one part of the phishing kit found. This is to create a .session files of user and bot to interact with the Telegram API

# Main feeds of this program
In general terms, the core of telegram-hitbackscammer are the chat/channels and Telegram bot tokens. Below you can see some examples taken from real cases:

Public channel:
```diff
//bot token
var telegram_bot_id =  "4509046619:LMnjdorkaLUIiJldlp302lJDLmciOlLjJsi";
//chat id
var chat_id ="@diner0facilk";
```

Private chat/channel:
```diff
//bot token
var telegram_bot_id =  "5919290478:AAKiogpUidLGIMdImjI3V38roCOldLjsiOP";
//chat id
var chat_id ="5616310229";
```

So the values of bot and chat values without the quotes "" are the ones you need to get fun }:-)

# Requirements
* Python 3.7 or higher
* Internet Connection (You are going to be communicating with Telegram's servers)

# FAQ
### 1. Why do I have to login with my phone?

To interact with Telegram, you can do it as yourself (own entity) and with a bot.
All the scripts are using the bot-token of the scammer you found mainly to conduct the activities, the only script which uses your phone login is to read (not delete) the messages of public channels.

Take into account you need your mobile phone also to get an API key from Telegram, otherwise you won't be able to do anything with the API and these scripts.

### 2. Ok but, is my identity would be pwned, or found by the scammer/phisher?

Nope, the attackers won't have any information about you, despite we are doing something to the attacker's chat/channel, remember we are using their own bot and on the other hand, the communication takes places against Telegram using the API.

### 3. Can I use each script separately?

Yes you can, but I kindly suggest you to use the main one with the menu as a help for you, it's up to you :)

# Contact
Twitter: [@avechuch0](https://twitter.com/avechuch0)
