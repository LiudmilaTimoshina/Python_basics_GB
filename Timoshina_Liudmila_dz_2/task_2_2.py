#2.Дан список: ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками
# (добавить кавычку до и кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
# Сформировать из обработанного списка строку: в "05" часов "17" минут температура воздуха была "+05" градусов
# Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как модифицировать это условие для чисел со знаком?
# Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже. Главное: дополнить числа до двух разрядов нулём!

word_list = ['в','5','часов','17','минут','температура','воздуха','была','+5','градусов']

for word in word_list:
    if word.isnumeric() or word[0] == '+':
        if word[0] == '+':
           word_f = f'"+{int(word):02d}"'
        else:
            word_f = f'"{int(word):02d}"'
        word_idx = word_list.index(word)
        word_list[word_idx] = word_f
print(' '.join(word_list))




