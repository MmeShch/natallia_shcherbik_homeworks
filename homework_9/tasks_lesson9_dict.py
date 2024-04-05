# Задание1
# Создайте словарь person, в котором будут присутствовать ключи name, age, city. Выведите значение возраста из person.

# person = {
#     'name': 'Ann',
#     'age': 18,
#     'city': 'Boston'
# }
# print(person['age'])

# person = {
#     'name': 'Ann',
#     'age': 18,
#     'city': 'Boston'
# }
# try:
#     person['color']
# except KeyError:
#     print('Такого ключа нет')

# Задание2
# Значениями словаря могут быть и списки. Создайте словарь с ключами BMW, Tesla и списками из 3х моделей в качестве
# значений. Выведите первое и последнее значения каждого из ключей.

# cars = {
#     'BMW': ['x5', 'x3', 'x6'],
#     'Tesla': ['model 3', 'model s', 'model x']
# }
# for key in cars:
#     print(f'{cars[key][0]}, {cars[key][-1]}')

# Задание3
# Исправьте ошибки в коде, чтобы получить требуемый вывод. (Вывод True)
# d1 = {"a": 100. "b": 200. "c":300}
# d2 = {a: 300. b: 200, d:400}
# print(d1["b"] == d2["b"))

# d1 = {'a': 100, 'b': 200, 'c': 300}
# d2 = {'a': 100, 'b': 200, 'c': 300}
# print(d1['b'] == d2['b'])


# Задание4
# Дан словарь с числовыми значениями. Необходимо их все перемножить и вывести на экран.

# dict1 = {
#     'year': 1964,
#     'month': 12,
#     'day': 5
# }
# product = 1
# for value in dict1.values():
#     product *= value
# print(product)

# dict2 = {item: item ** 2 for item in range(1, 10)}
# print(dict2)
# product = 1
# for item in dict2.values():
#     product *= item
# print(product)


# Задание5
# Даны два списка одинаковой длины. Необходимо создать из них словарь таким образом, чтобы элементы первого списка были
# ключами, а элементы второго- соответственно значениями нашего словаря.

# list1 = [random.randint(50, 80) for i in range(1, 10)]
# list2 = [random.randint(40, 100) for j in range(1, 10)]
# my_dict = dict(zip(list1, list2))
# print(my_dict)

# Задание 6
# Создайте словарь из строки 'pythonist' следующим образом: в качестве ключей возьмите буквы строки, а значениями
# пусть будут числа, соответствующие количеству вхождений данной буквы в строку.

# string = 'pythonist'
# new_dict = {key: string.count(key) for key in string}
# print(new_dict)


#Задание 7
#Разработайте программу, которая будет переводить несколько слов с русского языка на английиский

dict = {
    'кот': 'cat',
    'собака': 'dog',
    'птица': 'bird',
    'рыба': 'fish'
}
input_rus_word = input('Введите слово на русском языке: ').lower()
if input_rus_word in dict:
    print(f'{dict[input_rus_word]}')
else:
    print(f'Нет такого слова в словаре')