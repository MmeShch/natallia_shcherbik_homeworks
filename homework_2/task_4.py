# Разделить строку "Apples, Oranges, Pears, Bananas, Berries" по запятым и вывести на экран
string = 'Apples, Oranges, Pears, Bananas, Berries'
string_split = string.split(',')
print(string_split)
# Объединить элементы с использованием пробела, чтобы программа вывела Apples Oranges Pears Bananas Berries
string_join = ' '.join(string_split)
print(string_join)
