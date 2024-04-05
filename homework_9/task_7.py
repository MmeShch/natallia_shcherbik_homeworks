# 7) Создать множество. Создать неизменяемое множество. Выполнить операцию объединениясозданных множеств. Выполнить
# операцию пересечения созданных множеств.
import random

set1 = {random.randint(1, 50) for x in range(9)}
print(set1)
set2 = frozenset({1, 2, 5, 100, 200, 300})
print(set2)
set3 = set1 | set2
print(set3)
print(set1 & set2)