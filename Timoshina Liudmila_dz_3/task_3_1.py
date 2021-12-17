# Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.

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

def num_translate(num_eng):
    return print(numbers.get(num_eng))

num_translate('eleven')
