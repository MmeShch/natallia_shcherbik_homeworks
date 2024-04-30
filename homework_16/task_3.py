# 3) Задача на декоратор
#
# метод sum(a, b) принимает 2 числа и возвращает их сумму.
# Написать декоратор, который возвращает ошибку
# если переданы не числовые параметры(например строка)
# пример:
#
# @validate_int_parameters
# def sum(a,b)`
#
# sum(3, "1") => ошибка
# sum(4, 2) = > 6


def validate_int_parameters(function):
    def wrapper(a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            return 'Error: No numeric parameters. Provide numeric values'
        return function(a, b)
    return wrapper


@validate_int_parameters
def summ(a, b):
    return a + b

print(summ(5, "k"))
print(summ(5, 6))
