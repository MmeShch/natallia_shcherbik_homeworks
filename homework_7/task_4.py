# 4) Дан список чисел. Выведите значение наибольшего элемента в списке, а затем индекс
# этого элемента в списке. Если наибольших элементов несколько, выведите индекс первого из них.
import random

# digits = [random.randint(1, 40) for i in range(20)]
# print(digits)
# max_elem = max(digits)
# print(f'The largest element in list is {max_elem}')
# print(f'The index of the largest element in list is {digits.index(max_elem)}')

# 2й способ

digits = [random.randint(1, 80) for i in range(10)]
print(digits)
ind = 0
max_elem = digits[0]
for i in range(1, len(digits)):
    if digits[i] > max_elem:
        max_elem = digits[i]
        ind = i
print(f'Max element in list is {max_elem} and the index of max element is {ind}')
