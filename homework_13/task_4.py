# 4) Напишите программу, которая подключает модуль math и, используя значение числа piπ
#  из этого модуля, находит для переданного ей на стандартный ввод радиуса круга периметр этого круга и выводит его
# на стандартный вывод.

import math

def find_circle_perim(radius):
    perimeter = 2 * math.pi * radius
    return round(perimeter, 2)


inp_radius = float(input('Enter a radius of a circle: '))
perim = find_circle_perim(inp_radius)
print(f'The perimeter of the circle is {perim}')

