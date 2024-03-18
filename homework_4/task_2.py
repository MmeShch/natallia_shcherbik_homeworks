#Определить существование треугольника
print('Введите значения сторон треугольника:')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and a + c > b and b + a > c:
    print('Треугольник существует')
else:
    print('Треугольник не существует')
