#5) Имеются два списка, сгенерированные случайным образом. Добавьте в конец первого списка все элементы второго списка.
import random

# list1 = [i+j for i in [1, 2, 8] for j in [400, 100]]
# list2 = [i+j for i in ['hi ', 'welcome '] for j in ['bye']]
# list1.extend(list2)
# print(list1)

#6) Из заранее сформированного списка следует удалить элемент, введенный пользователем.

# list1 = [i for i in range(10)]
# print(f'The first list is {list1}')
# item = int(input('Enter an item from list: '))
# for i in list1:
#     if i == item:
#         list1.remove(i)
# print(f'New list after removing is {list1}')

#7) Из исходного списка следует удалить элемент, позицию которого указал пользователь.

# list2 = [random.randint(1, 60) for i in range(8)]
# print(f'Random list {list2}')
# position = int(input('Enter a position for removing: '))
# if position < len(list2):
#         list2.pop(position)
# print(f'New list after removing a position {list2}')

# 8) В кортеже целых чисел вычислите произведение отрицательных элементов, имеющих нечетные индексы.

# tuple1 = (1, -5, 3, 8, -12, 89, -11, -125)
# print(f'There is a tuple {tuple1}')
# product = 1
# for i in range(1, len(tuple1), 2):
#     if tuple1[i] < 0:
#         product *= tuple1[i]
# print(f'Product of negative items in tuple is {product}')

# 9) Заполните один кортеж десятью случайными целыми числами от 0 до 5 включительно. Также заполните второй кортеж
# числами от -5 до 0. Объедините два кортежа с помощью оператора +, создав тем самым третий кортеж. С помощью метода
# кортежа count() определите в нем количество нулей. Выведите на экран третий кортеж и количество нулей в нем.

# first_t = tuple([random.randint(0, 5) for i in range(10)])
# second_t = tuple([random.randint(-5, 0) for i in range(10)])
# print(f'The first tuple is {first_t}\nThe second tuple is {second_t}')
# third_t = first_t + second_t
# print(f'The third tuple is {third_t}\nThe number of "0" in third tuple is {third_t.count(0)}')

# 10) Вывести данные кортежа без скобок, через запятую. Обязательно: элементы кортежа – строки.

# my_tuple = ('elements', 'strings', 'items', 'words')
# print(",".join(my_tuple))

# 11) Сгенерируйте 2 кортежа случайными числами в диапазоне от 10-90.Количество элементов в кортеже 10. Определить:
# 1) Сумма элементов какого из кортежей больше и вывести соответствующее сообщение на экран (Сумма больше в кортеже - ..)
# 2) Вывести на экран порядковые номера минимальных элементов этих кортежей

tup1 = tuple([random.randint(10, 90) for i in range(10)])
tup2 = tuple([random.randint(10, 90) for i in range(10)])
print(f'First tuple {tup1}\nSecond tuple {tup2}')

if sum(tup1) > sum(tup2):
    print(f'The sum of items is greater in the first tuple {tup1}')
else:
    print(f'The sum of items is greater in the second tuple {tup2}')
print(tup1.index(min(tup1)))
print(tup2.index(min(tup2)))



