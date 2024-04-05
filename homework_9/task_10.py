# 10) Создайте 2 множества:
# - Если они одинаковые: вывести что они равны
# - Если 1 множество полностью состоит из второго: вывести сообщение множество 1 состоит из множества2
# - Если 2 множество полностью состоит из 1: вывести сообщение множество 2 состоит из множества 1
# - Если они пересекаются: вывести элементы в которых они пересекаются
# - Если не пересекаются: вывести сообщение об этом
import random

set1 = {x * 3 for x in range(1, 25)}
set2 = {random.randint(1, 10) for j in range(20)}
set3 = {}
print(f'Set {set1}\nSet {set2}')
if set1 == set2:
    print(f'Set {set1} equal to set {set2}')
elif set1.issubset(set2):
    print(f'Set {set1} is a part of set {set2}')
elif set2.issubset(set1):
    print(f'Set {set2} is part of set {set1}')
elif set1 & set2:
    set3 = set1 & set2
    print(f'New set {set3}')
else:
    print('These sets do not have intersections')

