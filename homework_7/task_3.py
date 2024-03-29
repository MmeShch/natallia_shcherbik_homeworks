#3) Дан список чисел. Определите, сколько в этом списке элементов, которые больше
# двух своих соседей, и выведите количество таких элементов. Крайние элементы
# списка никогда не учитываются, поскольку у них недостаточно соседей.
import random

lst_nums = [random.randint(1, 30) for i in range(20)]
print(lst_nums)
counter = 0
for i in range(1, len(lst_nums) - 1):
    if lst_nums[i - 1] < lst_nums[i] > lst_nums[i + 1]:
        counter += 1
print(f"Quantity of items that are bigger than their neighbors: {counter}")

