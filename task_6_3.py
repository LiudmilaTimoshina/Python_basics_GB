#3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
# Известно, что при хранении данных используется принцип: одна строка — один пользователь,
# разделитель между значениями — запятая.
# Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО,
# значения — данные о хобби. Сохранить словарь в файл.
# Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО,
# задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1».
# При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.

from itertools import zip_longest
import json

with open('users.csv', 'r', encoding='utf-8') as name,\
        open('hobby.csv', 'r', encoding='utf-8') as hobby:
            names = name.read().splitlines()
            hobbys = hobby.read().splitlines()

if len(names) < len(hobbys):
    print(1)
else:
    users_hobby = dict(zip_longest(names, hobbys, fillvalue=None))
    print(users_hobby)
    with open('users_hobby_dict.txt', 'w') as f:
        json.dump(users_hobby, f, ensure_ascii=False)