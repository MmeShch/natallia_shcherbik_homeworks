# 2)На вход функция more_than_five(lst) получает список из целых чисел.
# Результатом работы функции должен стать новый список,
# в котором содержатся только те числа, которые больше 5 по модулю.

def more_than_five(lst):
    lst2 = []
    for num in lst:
        if abs(num) > 5:
            lst2.append(num)
    return f'List with numbers that are more than five by modulus {lst2}'


my_list = [i for i in range(-10, 10)]
print(more_than_five(my_list))
print(more_than_five([-100, 13, 0, 50, -2, -1, 14]))
