# 3) Если в функцию передаётся кортеж, то посчитать длину всех его слов. Если список, то посчитать кол-во букв и
# чисел в нём. Число - кол-во нечётных цифр. Строка - количество букв. Сделать проверку со всеми этими случаями

def foo(smth):
    if isinstance(smth, tuple):
        return 'Сумма длин все слов', sum([len(word) for word in smth])
    elif isinstance(smth, list):
        return 'Сумма букв и чисел в списке', len([item for item in smth if str(item).isdigit() or str(item).isalpha()])
    elif isinstance(smth, int):
        return 'Количество нечетных чисел', len([digit for digit in str(smth) if digit in "13579"])
    elif isinstance(smth, str):
        return 'Количество букв', len(smth)
    else:
        return 'Type is not defined'


print(foo(('hello', 'world', 'home', 'travel')))
print(foo([1, 'hello', 15, 'world', 129]))
print(foo(4568))
print(foo('delivery'))
