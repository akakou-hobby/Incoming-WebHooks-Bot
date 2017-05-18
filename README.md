# Incoming-WebHooks-Bot
## What is it
Python Modeule for Incoming WebHooks Bot.  
You can send to slack with Incoming WebHooks !  

## How to install
### First
This modeule can set to set move your program's directry.

### requests Modeule
You must install `requests` module to use this modeule.
Install `pip` and run this command.
```shell
pip install requests
```

## How to use
### Source
```python
bot = incoming_webhooks.IncomingWebhooks(url, text, username, icon_emoji, link_names)
bot.send()
```
### Meaning of each variable
* url : incoming webhooks URL  
* text : message you want to send
* username : bot name
* icon_emoji : bot icon
* link_names : if you want mention, input 1.


## Example
```python
# coding:utf-8

import incoming_webhooks

# Property
url = "https://hooks.slack.com/services/"
text = "hello"
username = "bot"
icon_emoji = ":+1:"
link_names = 1

# Run
bot = incoming_webhooks.IncomingWebhooks(url, text, username, icon_emoji, link_names)
bot.send()
```
