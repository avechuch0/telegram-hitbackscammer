# Telegram-hitbackscammer 
This is a set of scripts and protocols to do some offensive countermeausures and active defense against phishers/scammers who use Telegram chats/channels as part of phishing kits.

telegram-hitbackscammer.py is a practical application of Annoyance, Attribution and Attack core concepts to screw up threat actor activities, which can help on combating data theft, financial fraud prevention, impersonation, save people data, and contributing for a world wiping of phishing :)

Want more information around this concepts:

https://icdt.osu.edu/offensive-countermeasures-art-active-defense

https://en.wikipedia.org/wiki/Active_defense

https://www.sans.org/white-papers/36240/

https://www.slideshare.net/JaimeAndrsBelloVieda/una-mirada-a-la-active-defense-harbinger-distribution-como-herramienta-de-monitoreo-y-defensa-activa-ante-ataques

# Quick Overview
Default mode - Running *telegram-hitbackscamer.py*

![alt text](https://github.com/avechuch0/telegram-hitbackscammer/blob/main/images/main.png)

# Options Description
## 1. Doubts? - Check if the channel is public or private
Scammers/phishers use multiple options to store the data on Telegram once a victim trips up on tramp. The options vary between public/private channels and private chats. It is easy to find a Telegram public channel on a phishing kit, you will see an @ at the begging or simply you can search through your Telegram App for the channel. Private chats/channels identifiers are composing by numbers ALWAYS.

But anyway, this option is precisely to check it, so let telegram-hitbackscammer do it for you.

More info around about the Telegram chats/channels https://telegram.org/faq_channels

## 2. Get the list of administrators for channel
Get a table of administrators of scammer channel, depending of the case and the permissions of the bot, may you can see who is the owner of the channel and conclude some attribution to a threat actor.

## 3. Delete the last 48 hours messages of public channel  - (Only for public channels)
Selecting this option, you can read and delete up to the last 48 hours of messages of **public** scammer channel. **Be sure to input a public channel once you are asked if you want to avoid errors.**

## 4. Delete the last 48 hours messages of private channel - (Only for private channels)
Selecting this option, you can read and delete up to the last 48 hours of messages of **private** scammer channel. **Be sure to input a private channel once you are asked if you want to avoid errors.**

## 5. Listening mode for bot to delete any incoming messages
This is an interesting option if you want to annoy the scammer a lot!

This option has the power to inmediately delete any try posting message the scammer bot would like to store on channel/chat. No matter what channel/chat id you already found on the phishing, this has the plus of **deleting inmediately the messages for any post in any channel/chat the scammer has set up.**

Once you select this option you will see the message "Listening mode for bot", and any time a victim inputs data on a phishing associated with the bot-token value, you would be notified on the shell with a successfully message deletion, while the scammer would be fucked up and unable to see what the bot tried to post.

## 6. Leave the channel - (Available for both Public/Private channels)
This simply unattach/leave the scammer channel where the bot is linked. This is a silent annoying way to avoid further posting for bot on the channel, but has 2 disadvantages.
1. The scammer/phisher would not be notified about this action, but once he/she checks the list of administrators, they would realize what happened, it's up to them include again the bot or not.
2. **And the most important disadvantage** Once you leave a channel, you won't be able to do anything else on the channel. **This should be your last option/decision due the lack of control once you leave.**

# Getting started
1. Download / clone the repo
2. Install required packages: pip3 install -r requirements.txt
3. Get the Telegram API keys (api_id and api_hash) following the instructions here https://core.telegram.org/api/obtaining_api_id
4. Set the API keys in your config.ini file
5. You're ready to go :) simply run the main script *python .\telegram-hitbackscammer.py* or *python3 .\telegram-hitbackscammer.py* depending how you are calling your python instance.

# Requirements
* Python 3.7 or higher
* Internet Connection (You are going to be communicating with Telegram's servers)

