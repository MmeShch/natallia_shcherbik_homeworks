# 8)Необходимо с помощью цикла while вывести данную последовательность чисел: 1 2 4 8 16 32 64 128 256 512
list1 = []
number = 1
while number <= 512:
    list1.append(number)
    number *= 2
print(list1)