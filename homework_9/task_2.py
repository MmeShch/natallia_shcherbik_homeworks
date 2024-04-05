# 2) Создайте словарь d = {'1': 0, ‘2’: 0, '3': 0} тремя способами. Выведите полученный словарь на экран.

# 1.
# keys = ['1', '2', '3']
# values = [0, 0, 0]
# d = dict(zip(keys, values))
# print(f'New dictionary {d}')

# 2.
# d = dict([('1', 0), ('2', 0), ('3', 0)])
# print(f'New dictionary {d}')

# 3.
# keys = ['1', '2', '3']
# d = dict.fromkeys(keys, 0)
# print(f'New dictionary {d}')

# 4.
# str = '1 2 3'
# my_dict = {n: int(n) * 0 for n in str.split()}
# print(f'New dictionary is {my_dict}')

