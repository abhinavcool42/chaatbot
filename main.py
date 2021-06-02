import discord
import os
#import chatterbot
#import chatterbot_corpus

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

from keep_alive import keep_alive

chatbot = ChatBot("nick")
bot = discord.Client()

trainer = ChatterBotCorpusTrainer(chatbot.storage)
trainer.train("chatterbot.corpus.english")

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
      await msg.reply(temp)


keep_alive()
token = os.environ.get("TOKEN")
bot.run(token)
#bot.run(os.getenv('TOKEN'))