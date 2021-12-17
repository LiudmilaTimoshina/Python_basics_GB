# Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого)

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

from random import sample

def get_jokes_2(n):
    jokes = []
    nn_list = sample(nouns,n)
    adv_list = sample(adverbs,n)
    adj_list = sample(adjectives,n)
    for nn, adv, adj in zip(nn_list, adv_list, adj_list):
        print(f'{nn} {adv} {adj}')

get_jokes_2(5)



