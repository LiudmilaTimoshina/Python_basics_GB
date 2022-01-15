#4. Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции
# и выбрасывать исключение ValueError, если что-то не так

from functools import wraps

def val_checker(l_func):
    def _val_checker(func):
        @wraps(func)
        def wrapper(num):
            if l_func(num):
                res = func(num)
            else:
                raise ValueError (f'wrong value: {num}')
            return res

        return wrapper

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3

print(calc_cube(-5))