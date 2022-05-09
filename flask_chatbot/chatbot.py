from chatterbot import ChatBot
# import chatbot
from pytz import UTC
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import time
time.clock = time.time
# Creating ChatBot Instance
CB = ChatBot('ChatBot')


 # Training with Personal Ques & Ans
conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "You're welcome.",
    "who Developed you",
    "I am Developed by Abdul Manaf PV",
    "what are the your services",
    "Our services:"
    "> Digital Marketing"
    "> Web Designing "
    "> Graphic Designing ",
]
trainer = ListTrainer(CB)
trainer.train(conversation)
# # Training with English Corpus Data
trainer_corpus = ChatterBotCorpusTrainer(CB)
trainer_corpus.train('chatterbot.corpus.english')