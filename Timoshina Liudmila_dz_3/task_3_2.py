numbers = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}

def num_translate_adv(num_eng):
    if num_eng[0].isupper():
        print(numbers.get(num_eng.lower()).capitalize())

num_translate_adv('One')