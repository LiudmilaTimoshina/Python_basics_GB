#3.Написать декоратор для логирования типов позиционных аргументов функции
#from functools import wrap

def type_logger(func):
    def wrapper(num):
        res = func(num)
        print(f'{func.__name__} ({num} {type(num)})')
        return res
    return wrapper

@type_logger
def calc_cube(x):
    return x

a = calc_cube(5)
print(a)