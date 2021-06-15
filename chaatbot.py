import os
import pymongo

mon_user=os.environ.get("MON_USER")
mon_pass=os.environ.get("MON_PASS")

uri = f'mongodb+srv://{mon_user}:{mon_pass}@chaat.qvbi4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
myclient = pymongo.MongoClient(uri)
mydb = myclient["chaat-db"]

#chaat=mydb['dataBS']

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot("nick",
storage_adapter='chatterbot.storage.MongoDatabaseAdapter', 
logic_adapters=["chatterbot.logic.BestMatch","chatterbot.logic.TimeLogicAdapter","chatterbot.logic.MathematicalEvaluation"], 
database_uri=f'mongodb+srv://{mon_user}:{mon_pass}@chaat.qvbi4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

trainer = ChatterBotCorpusTrainer(chatbot.storage)
trainer.train("chatterbot.corpus.english")

