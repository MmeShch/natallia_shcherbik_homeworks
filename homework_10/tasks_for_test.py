# 1
import math

# x = float(input('Enter 1st number: '))
# y = float(input('Enter 2nd number: '))
# result = (abs(x) - abs(y)) / (1 + abs(x * y))
# print(result)

# 2 Даны катеты прямоугольного треугольника. Найти его гипотенузу и площадь.

# c1 = float(input('Enter 1st cathetus: '))
# c2 = float(input('Enter 2nd cathetus: '))
# h = math.sqrt(c1 ** 2 + c2 ** 2)
# A = 1/2 * c1 * c2
# print(f'Hypotenuse is {h} \nTriangle area is {A}')

# 3 Создать переменные a, b, c и присвоить им значения 9, 17 и 5 соответственно. Проверить выполнение следующих условий:
# a больше b
# a не равно разности b и c
# b равно сумме a и c
# c меньше или равно сумме a и b
# a меньше b, но больше c
# b больше a или b больше c

# a = 9
# b = 17
# c = 5
# if a > b:
#     print(f'{a} greater than {b}')
# elif a != (b - c):
#     print(f'{a} is not equal to {(b - c)}')
# elif b == (a + c):
#     print(f'{b} is equal to {(a + c)}')
# elif c <= (a + b):
#     print(f'{c} is lower or equal than {(a + b)}')
# elif c < a < b:
#     print(f'{a} is lower than {b} and greater than {c}')
# elif b > a or b > c:
#     print(f'{b} is greater than {a} or {b} is greater than {c}')

# 4 Перевести строку в список по пробелу "Robin Singh" => ["Robin”, “Singh"]
# "I love arrays they are my favorite" => ["I", "love", "lists", "they", "are", "my", "favorite"]

# my_list1 = "Robin Singh".split(" ")
# print(my_list1)
# my_list2 = "I love arrays they are my favorite".split(" ")
# my_list2[2] = 'lists'
# print(my_list2)

# 5 Дан список ["I", "love", "lists", "they", "are", "my", "favorite"] сделайте из него строку =>
# "I love arrays they are my favorite"

# list1 = ["I", "love", "lists", "they", "are", "my", "favorite"]
# str1 = " ".join(list1)
# str1 = str1.replace('lists', 'arrays')
# print(str1)

# 6 Даны несколько списков: [-8, 1, 2, -2, 0], [1, -1, 0, -9, 4, -5], [1, 4, 0, 23, 6, 34].
# Для каждого из списков найти второе наименьшее значение в нем (правильные ответы выделены жирным шрифтом).

# list1 = [-8, 1, 2, -2, 0]
# list2 = [1, -1, 0, -9, 4, -5]
# list3 = [1, 4, 0, 23, 6, 34]
# for i in (list1, list2, list3):
#     i.sort()
#     the_2_smallest = i[1]
#     print(f'The second smallest value in list is {the_2_smallest}')
#

# 7 Дан список цветов: ‘red’, ‘green’, ‘white’, ‘black’, ‘pink’, ‘yellow’. Создайте еще один список и
# переместите в него 1-ый, 5-ый и 6-ой элементы.

# colors = ['red', 'green', 'white', 'black', 'pink', 'yellow']
# colors2 = []
# colors2.append(colors[0])
# colors2.append(colors[4])
# colors2.append(colors[5])
# print(colors2)

# 8 Даны два целых числа m и n. Напишите программу, которая выводит все числа от m до n
# включительно в порядке возрастания, если m<n, или в порядке убывания в противном случае.

# m = int(input('Enter 1st whole number: '))
# n = int(input('Enter 2nd whole number: '))
# if m < n:
#     for i in range(m, n + 1, 1):
#         print(i)
# else:
#     for i in range(m, n - 1, -1):
#         print(i)

# 9 С помощью цикла while просите пользователя решить пример, пока он не введет правильный ответ.
#Так же у пользователя есть заданное количество попыток. Если он их использовал, то вывести об этом сообщение
# Пример:
# 	решите задачу: 3+4-7=?
# 	>>>1
# 	>>> Неверное решение
# 	>>>2
# 	>>> Неверное решение
# 	>>>7
# 	>>> Неверное решение
# 	>>>0
# 	>>> Правильно.
# 	>>>Выходим из приложения
# Пример2:
# 	решите задачу: 3+4-7=?
# 	кол-во попыток:3
# 	>>>1
# 	>>> Неверное решение
# 	>>>2
# 	>>> Неверное решение
# 	>>>7
# 	>>> Неверное решение.
# 	>>> У вас закончились попытки. Выходим из приложения

# attempts = 0
# correct_answer = 0
# while attempts < 3:
#     input_user = int(input('Solve the problem: 3+4-7= \n'))
#     if input_user == correct_answer:
#         print('You are right!')
#         print('Leave the application')
#         break
#     else:
#         attempts += 1
#         print('Incorrect solution!')
# if attempts >= 3:
#     print('You have run out of attempts. Please leave the application')

# 10 Дан список чисел [1, 2, 3, 20, 30, 45, 20, 100, 20], необходимо удалить все вхождения числа 20 из него.

# the_list = [1, 2, 3, 20, 30, 45, 20, 100, 20]
# for i in the_list:
#     if i == 20:
#         the_list.remove(i)
# print(the_list)

# 11 Заполнить список ста нулями, кроме первого и последнего элементов, которые должны быть равны единице

# new_list = [0 for i in range(1, 99)]
# new_list[0] = 1
# new_list[-1] = 1
# print(new_list)

# 12 Сформировать возрастающий список из чётных чисел (количество элементов 45)

# my_list = [i for i in range(0, 90, 2)]
# print(my_list)

# my_list = [i * 2 for i in range(45)]
# print(my_list)

# 13 Есть список a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]. Выведите все элементы, которые меньше 5.

# list_a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# list_b = []
# for a in list_a:
#     if a < 5:
#         list_b.append(a)
# print(list_b)

# 14 Заполнить список степенями числа 2 (от 2^1 до 2^n)

# n_power = int(input('Enter a power: '))
# list1 = [2 ** i for i in range(1, n_power + 1)]
# print(list1)

# 15 Дан словарь с числовыми ключами и значениями. Необходимо их все ключи перемножить а значения сложить и
# вывести на экран.

# my_dict = {item: item * 2 for item in range(1, 15)}
# print(my_dict)
# prod_key = 1
# for key in my_dict.keys():
#     prod_key *= key
# print(f'Product of keys is {prod_key}')
# sum_val = 0
# for value in my_dict.values():
#     sum_val += value
# print(f'The sum of values is {sum_val}')

# 16 Создайте словарь, в котором ключами будут числа от 1 до 10, а значениями эти же числа, возведенные в куб.

# my_dict = {x: x ** 3 for x in range(1, 10)}
# print(my_dict)

# 17 Напишите программу, которая получает на вход две строки с перечислением интересов и хобби двух пользователей,
# и вычисляет процент совпадения.

# hobbies1 = input('Enter your hobbies: ').split()
# hobbies2 = input('Enter your friend hobbies: ').split()
# match_result = len(set(hobbies1).intersection(set(hobbies2))) / len(set(hobbies1).union(set(hobbies2))) * 100
# print(f'The match rate is {match_result}%')

# hobbies1 = 'soccer football running reading'.split()
# hobbies2 = 'reading chess travelling swimming'.split()
# print(f'{hobbies2}\n{hobbies1}')
# common_hobbies = []
# for i in hobbies1:
#     if i in hobbies2:
#         common_hobbies.append(i)
# total_hobbies = hobbies1.copy()
# for i in hobbies2:
#     if i not in hobbies1:
#         total_hobbies.append(i)
# match_hobbies = len(common_hobbies) / len(total_hobbies) * 100
# print(f'The match rate is {match_hobbies}%')


# 18 Напишите программу, которая получает n слов, и вычисляет количество уникальных символов во всех словах.

# n = int(input('Enter number of words: '))
# print('Unique chars in all words:', len(set(''.join([input('Enter a word: ').lower() for _ in range(n)]))))





    

