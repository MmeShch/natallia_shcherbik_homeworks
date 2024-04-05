# 1) Проверить, есть ли у последовательности дубликаты?

# my_list = [2, 8, 8, 'h', 3, 'h']
# my_set = set(my_list)
# if len(my_list) == len(my_set):
#     print(f'All the elements are unique in {my_list}')
# else:
#     print(f'There are duplicates in {my_list}')


# 2) Напишите программу, которая создает пустое множество и заполняет его 10 случайными целыми числами от 1 до 20.
# Затем выведите это множество на экран.

# my_set = {random.randint(1, 20) for i in range(11)}
# print(my_set)

# my_set = set()
# while len(my_set) < 10:
#     my_set.add(random.randint(1, 20))
# print(my_set)

# 3) Вам необходимо создать 2 множества а затем из двух этих множеств получить третье множество таким образом,
# чтобы новое множество содержало только те элементы, которые есть в обоих исходных множествах.

# set1 = {i for i in range(10)}
# set2 = {i**2 for i in range(15)}
# print(f'{set1}\n{set2}')
# set3 = set1 & set2
# print(f'New set with common elements {set3}')

# 4) Напишите программу, которая проверяет, является ли одно множество подмножеством другого множества.

# set1 = {1, 3, 8, 125, 14, 20}
# print(set1.issubset({1, 3, 'j', 125, 14, 'f', 'h', 'z', 20, 8}))


# 5) Напишите программу, которая будет из  генерировать множество а на выходе программа должна вернуть возвращает
# список, содержащий все элементы этого множества, умноженные на 2.

# my_set = {random.randint(5, 13) for x in range(8)}
# print(my_set)
# my_list = []
# for x in my_set:
#     my_list.append(x * 2)
# print(f'New list with elements multiplied by 2: {my_list}')


# 6) Создайте два множества из списка слов "apple", "banana", "orange", "grape", "kiwi" и "banana". Выведите на
# экран разность этих множеств.

# fruits = ["apple", "banana", "orange", "grape", "kiwi", "banana"]
# set1 = set(fruits)
# fruit = ["banana"]
# set2 = set(fruit)
# print(f'Set 1 is {set1}\nSet 2 is {set2}')
# set3 = set1.difference(set2)
# print(f'Set 3 is difference: {set3} ')

# 7) Напишите программу, которая удаляет все дубликаты из списка и создает из него множество.

# my_list = [1, 'y', 1, 10, 5, 9, 2, 2, 'y']
# print(my_list)
# my_set = set(my_list)
# print(f'New set with unique elements from list {my_set}')

# 8. Сгенерируйте два множества. Программа должна вернуть новое множество, содержащее все элементы из первого
# множества, которых нет во втором.

# set1 = {i ** 2 for i in range(13)}
# set2 = {j * 3 for j in range(14)}
# print(f'{set1}\n{set2}')
# set3 = set1 - set2
# print(set3)
