'''
import discord
import os
#import pymongo
#import chatterbot
#import chatterbot_corpus

from keep_alive import keep_alive
from chaatbot import chatbot

bot = discord.Client()

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_message(msg):
#avoid looping
    if msg.author==bot.user:
      return
    else:
      temp=chatbot.get_response(msg.content)
      if temp=='':
        await msg.reply('‎')
      else:
        await msg.reply(temp)

'''
keep_alive()
'''
token = os.environ.get("TOKEN")
bot.run(token)
#bot.run(os.getenv('TOKEN'))
'''