# Вычислить сумму цифр случайного трехзначного числа.
import random

num = random.randint(100, 999)
print(num)
d1 = num % 10
d2 = num % 100 // 10
d3 = num // 100
print(d1 + d1 + d2)



