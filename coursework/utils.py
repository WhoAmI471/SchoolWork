import requests
from random import choice
from config import WORD_ON_JSON
from basic_word import BasicWord


def load_random_word():
    response = requests.get(WORD_ON_JSON)
    word = response.json()

    data = choice(word)

    word = BasicWord(data['word'], data['subwords'])

    return word