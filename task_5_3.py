#3. Есть два списка. Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>).
# Количество генерируемых кортежей не должно быть больше длины списка tutors.
# Если в списке klasses меньше элементов, чем в списке tutors, необходимо вывести последние кортежи в виде: (<tutor>, None)

from itertools import zip_longest, islice

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
gen_tutors= ((tutors, klasses) for tutors, klasses in zip_longest(tutors, klasses,fillvalue=None))

print(*gen_tutors)
print(*islice(gen_tutors, len(tutors)), sep='\n')
