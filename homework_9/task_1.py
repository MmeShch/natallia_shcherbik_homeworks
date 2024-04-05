# 1) Даны два словаря: dictionary_1 = {'a': 300, 'b': 400} и dictionary_2 = {'c': 500, 'd': 600}.
# Объедините их в один при помощи встроенных функций языка Python.

# dict1 = {'a': 300, 'b': 400}
# dict2 = {'c': 500, 'd': 600}
# print(f'{dict1}\n{dict2}')
# dict3 = {**dict1, **dict2}
# print(f'{dict3}')

dict1 = {'a': 300, 'b': 400}
dict2 = {'c': 500, 'd': 600}
print(f'{dict1}\n{dict2}')
dict3 = dict1 | dict2
print(f'Merged new dictionary {dict3}')