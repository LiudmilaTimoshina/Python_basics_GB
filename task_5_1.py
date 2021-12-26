#1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield

def odd_num(n):
    for num in range(1, n + 1, 2):
        yield num


odd_to_15 = odd_num(15)
print(next(odd_to_15))
print(next(odd_to_15))
print(*odd_to_15)