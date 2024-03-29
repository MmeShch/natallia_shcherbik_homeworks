#1) Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.
numbers = [i for i in range(15)]
print(f'Сгенерирован список {numbers}')
new_numbers = []
for i in range(1, len(numbers)):
    if numbers[i] > numbers[i-1]:
        new_numbers.append(numbers[i])
print(f'Новый список {new_numbers}')

