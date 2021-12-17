# Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого)

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

from random import choice

def get_jokes(n):
    """Generate jokes consist of 3 random words"""
    jokes = []
    i = 0
    while i < int(n):
        joke = f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}'
        jokes.append(joke)
        i += 1
    print(jokes)

get_jokes(10)




