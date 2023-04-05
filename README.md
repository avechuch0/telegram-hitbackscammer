[![Active Development](https://img.shields.io/badge/Maintenance%20Level-Actively%20Developed-brightgreen.svg)](https://gist.github.com/cheerfulstoic/d107229326a01ff0f333a1d3476e068d)

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/avechuch0)

# Telegram-hitbackscammer 
This is a set of scripts and protocols to conduct active defense and offensive countermeasures activities against scammers/phishers who use Telegram chats/channels as part of phishing kits, to store the victim's stolen data.

telegram-hitbackscammer.py is a practical application of Annoyance, Attribution and Attack core concepts of active defense and offensive countermeausures to screw up threat actor activities, which can help with combating data theft, financial fraud prevention, impersonation, saving people's data, and contributing to a world free of phishing :)

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
If you don't know whether the channel found on the phishing kit is public or private, use this option to check it.

More info about the Telegram chats/channels: https://telegram.org/faq_channels

### 2. Get the list of channel administrators
Get a list of scammer channel`s administrators, then you may see who is the owner of the channel and make a threat attribution, i.e. identify the responsible scammer/phisher.

### 3. Delete the last 48 hours messages of a public channel  - (Only for public channels)
Selecting this option, you can read and delete the messages received during the last 48 hours on **public** scammer channel. Be sure to **input a public channel name** once the program asks to avoid errors.

### 4. Delete the last 48 hours messages of a private channel - (Only for private channels)
Selecting this option, you can read and delete the messages received during the last 48 hours on **private** scammer channel. Be sure to **input a private channel name** once the program asks to avoid errors.

### 5. Listening mode for bot to delete any incoming messages
This is an interesting option if you want to annoy the scammer!

This option has **the power to delete immediately any message the scammer bot writes in any chat/channel** associated with the malicious bot-token found on the phishing kit, if the attacker has more phishing campaings with other chats/channels created.

Once you select this option, you will see the message **Ok, Listening mode for bot**, and every time a victim processes the data on a phishing website associated with the bot-token value, you will see a notification on the shell/screen that the message was deleted. The scammer will be fucked up and unable to see what the bot tried to post in the chat/channel.

### 6. Leave the channel - (Available for both Public/Private channels)
This will disconnect/make a bot used by a scammer/phisher leave the channel. This is a way to avoid further bot's posting on the channel without your actions being noticed. This option **has 2 disadvantages** though:

1. The scammer/phisher would not be notified about this action, but once he/she checks the list of administrators, he/she would realize what happened. It's up to them to add again the bot or not to the channel.
2. And the most important disadvantage: </br>
Once you leave a channel, you won't be able to do anything else there. So this should be your last option.

### 7. Exit
Just to finish the program.

# Getting started
1. Download / clone the repo
2. Install required packages: ```pip3 install -r requirements.txt``` or ```pip install -r requirements.txt``` 
3. Get the Telegram API keys (api_id and api_hash) following the instructions here https://core.telegram.org/api/obtaining_api_id
4. Set the API keys in your config.ini file
5. You're ready to go :) simply run the main script ```python3 .\telegram-hitbackscammer.py``` for Linux or ```python .\telegram-hitbackscammer.py``` if you are using a Windows environment 
6. The first time, you would be asked for a kind of login, **input your mobile number** including the + (i.e. +57300...), then you would be asked for the bot-token (i.e. 4509046619:LMnjdorkaLUIiJldlp302lJDLmciOlLjJsi), found on the phishing kit. This is to create a .session files to interact with the Telegram API

# Main feeds of this program
The core of telegram-hitbackscammer are the chats/channels and Telegram bot-tokens. Below you can see some examples taken from real phishing cases:

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

So the bot token and chat id values without the quotes "" are the ones you need to have fun }:-)

# Requirements
* Python 3.7 or higher
* Internet Connection (You are going to be interacting with Telegram's servers)

# FAQ
### 1. Is my identity would be pwned, or found by the scammer/phisher?

Nope, the attackers won't have any information about you. Despite your possible actions on the attacker's chat/channel, remember we are using their own bot and, on the other hand, the communication takes place between the bot and Telegram through the API.

### 2. Why it can delete just the last 48 hours of messages?

Because it is working according to the current policy and limitations of Telegram Bot Api https://core.telegram.org/bots/api#deletemessage

### 3. Can I use each script separately?

Yes you can, but I kindly recommend you to use the main one with the menu, though it's up to you :)

# Contact
Twitter: [@avechuch0](https://twitter.com/avechuch0)
