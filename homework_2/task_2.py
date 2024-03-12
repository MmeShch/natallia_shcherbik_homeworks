# Вычислить сумму цифр случайного трехзначного числа. Применить работу со строками.
import random

num = random.randint(100, 999)
print(num)
d1 = str(num % 10)
d2 = str(num % 100 // 10)
d3 = str(num // 100)
num_1 = int(d1)
num_2 = int(d2)
num_3 = int(d3)
print(num_1 + num_2 + num_3)
