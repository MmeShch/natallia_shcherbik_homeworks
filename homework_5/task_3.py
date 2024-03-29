# 3)Даны несколько списков: [-8, 1, 2, -2, 0], [1, -1, 0, -9, 4, -5], [1, 4, 0, 23, 6, 34].
# Для каждого из списков найти второе наименьшее значение в нем

# 1 способ:
# a = [-8, 1, 2, -2, 0]
# b = [1, -1, 0, -9, 4, -5]
# c = [1, 4, 0, 23, 6, 34]
# print(f'Даны списки {a}, {b}, {c}')
# a.sort()
# b.sort()
# c.sort()
# print(f'Второе наименьшее значение каждого списка: {a[1]}, {b[1]}, {c[1]}')

# 2 способ:
a = [-8, 1, 2, -2, 0]
b = [1, -1, 0, -9, 4, -5]
c = [1, 4, 0, 23, 6, 34]
print(f'Даны списки {a}, {b}, {c}')
a = sorted([-8, 1, 2, -2, 0])
for i in a:
    if i != a[0]:
        print(f'Второе наименьшее значение первого списка: {i}')
        break
b = sorted([1, -1, 0, -9, 4, -5])
for i in b:
    if i != b[0]:
        print(f'Второе наименьшее значение второго списка: {i}')
        break
c = sorted([1, 4, 0, 23, 6, 34])
for i in c:
    if i != c[0]:
        print(f'Третье наименьшее значение третьего списка: {i}')
        break




