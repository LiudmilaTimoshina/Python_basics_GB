#4. Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ (разумеется, не нужно реально
# создавать такие большие файлы, это просто задел на будущее проекта). Также реализовать парсинг данных из файлов —
# получить отдельно фамилию, имя и отчество для пользователей и название каждого хобби: преобразовать в какой-нибудь
# контейнерный тип (список, кортеж, множество, словарь).

from itertools import zip_longest

with open('users.csv', 'r', encoding='utf-8') as name, \
        open('hobby.csv', 'r', encoding='utf-8') as hobby:
    names = name.read().splitlines()
    hobbys = hobby.read().splitlines()

users_hobbys = ((names, hobbys) for names, hobbys in zip_longest(names, hobbys, fillvalue=None))

with open('users_hobby_dict_2.txt', 'w') as f:
    for user_hobby in users_hobbys:
        f.write(f'{user_hobby[0]}: {user_hobby[1]}\n')