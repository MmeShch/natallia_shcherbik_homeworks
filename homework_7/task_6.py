# 6) В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент
# этого списка.
import random

elements = [random.randint(1, 15) for i in range(15)]
print(elements)
max_ind = elements[0]
min_ind = elements[0]
for i in range(1, len(elements)):
    if elements[i] > max_ind:
        max_ind = i
    elif elements[i] < min_ind:
        min_ind = i
elements[max_ind], elements[min_ind] = elements[min_ind], elements[max_ind]
print(elements)


