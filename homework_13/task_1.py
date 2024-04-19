#1) Функция для вывода таблицы умножения для указанного числа

# 1й способ:

# def mult_table(num):
#     for row in range(1, num+1):
#         for column in range(1, num+1):
#             print(row * column, end='\t')
#         print()
#
#
# number = int(input('Enter a number: '))
# mult_table(number)

# 2й способ:

# def mult_table(num):
#     for row in range(1, num+1):
#         for column in range(1, num+1):
#             print(f'{row} * {column} = {row * column}\t', end=' ')
#         print()
#
#
# number = int(input('Enter a number: '))
# mult_table(number)

# 3й способ: таблица умножения для одного числа, заданного пользователем

# def mult_table(num):
#     for k in range(1, num+1):
#         print(f'{num} * {k} = {num * k}')
#
#
# number = int(input('Enter a number: '))
# mult_table(number)