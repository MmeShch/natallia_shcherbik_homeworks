# 2)  Написать функцию, которая определяет количество разрядов введённого целого числа.

#1)
# def count_digit(num):
#     if num == 0:
#         return 1
#     count = 0
#     while num != 0:
#         count += 1
#         num //= 10
#     return count
#
#
# inp_num = int(input('Enter a number: '))
# digits = count_digit(inp_num)
# print(f'The number of digits is {digits}')

#2)
# def count_digits(number):
#     return len(str(number))
#
#
# inp_num = int(input('Enter a number: '))
# num_digits = count_digits(inp_num)
# print(f'The number of digits is {num_digits}')


# 3) Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран в одну строку
# значения, которые встречаются в нём более одного раза.

# def more_than_one(numbers):
#     duplicates = []
#     numbers = list(map(int, numbers.split()))
#     for i in range(len(numbers)):
#         for j in range(i+1, len(numbers)):
#             if numbers[i] == numbers[j] and numbers[i] not in duplicates:
#                 duplicates.append(numbers[i])
#     print(" ".join(map(str, duplicates)))
#
#
# more_than_one("1 3 5 9 9 17 17 20 20")



more_than_one('12345699111155')


