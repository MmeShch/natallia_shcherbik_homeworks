# 4) Напишите программу, которая вычисляет процентное содержание символов G (гуанин)
# и C (цитозин) в введенной строке (программа не должна зависеть от регистра вводимых символов).
# Например, в строке "acggtgttat" процентное содержание символов G и C равно 4/10 ⋅ 100 = 40.0
# где 4 - это количество символов G и C, а 10 -- это длина строки.

new_string = input('Enter a string with random quantity of "g" and "c": ').lower()
quantity = 0
for i in new_string:
    if i == 'c' or i == 'g':
        quantity += 1
percentage = quantity / len(new_string) * 100
print(f'Symbol percentage of "G" and "C" in string is {percentage}')




