# 5) Петя перешёл в другую школу. На уроке физкультуры ему понадобилось определить своё место в строю.
# Помогите ему это сделать. Программа получает на вход невозрастающую последовательность натуральных чисел,
# означающих рост каждого человека в строю. После этого вводится число X – рост Пети. Все числа во входных
# данных натуральные и не превышают 200. Выведите номер, под которым Петя должен встать в строй. Если в строю есть люди
# с одинаковым ростом, таким же, как у Пети, то он должен встать после них.
import random

line = [random.randint(150,200) for i in range(15)]
line.sort(reverse=True)
print(line)
height = int(input('Enter the height of Petya: '))
pos_of_height = 0
while pos_of_height < len(line) and line[pos_of_height] >= height:
    pos_of_height += 1
print(f'Position of Petya in line is {pos_of_height + 1}')
