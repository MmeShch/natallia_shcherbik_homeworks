# Дана следующая функция y = f(x). y = 2x – 10, если x > 0, y = 0, если x = 0, y = 2 *|x| - 1, если x < 0
# Примечание: для нахождения модуля используйте встроенную функцию abs(x)
print('Дана функция y = f(x)')
import math
x = int(input('Введите x: '))
if x > 0:
    y = 2 * x - 10
elif x == 0:
    y = 0
else:
    y = 2 * abs(x) - 1
print('y = ', y)


