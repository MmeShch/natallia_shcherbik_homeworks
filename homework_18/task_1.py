# Экземляр класса задается тройкой координат в трехмерном пространстве (x,y,z).
# Обязательно должны быть реализованы методы:
# – сложение векторов оператором `+` (метод __add__),
# – вычитание векторов оператором `-` (метод __sub__),
# – скалярное произведение оператором `*` (метод __mul__),
# – умножение на скаляр оператором `*` (метод __mul__),
# – векторное произведение оператором `@` (метод __matmul__)
# метод read - считывает координаты с клавиатуры
# метод display - Выводит на экран координаты
# Пример
# v1 = Vector3D(4, 1, 2)
# v1.display()
# v2 = Vector3D()
# v2.read()
# v3 = Vector3D(1, 2, 3)
# v4 = v1 + v2
# v4.display()
# a = v4 * v3
# print(a)
# v4 = v1 * 10
# v4.display()
# v4 = v1 @ v3
# v4.display()


class Vector3D:

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def display(self):
        print(f'{self.x}, {self.y}, {self.z}')

    def read(self):
        self.x = int(input('Enter x-coordinate: '))
        self.y = int(input('Enter y-coordinate: '))
        self.z = int(input('Enter z-coordinate: '))

    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if isinstance(other, Vector3D):
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:
            return Vector3D(self.x * other, self.y * other, self.z * other)

    def __matmul__(self, other):
        return Vector3D(self.y * other.z - self.z * other.y,
                        self.z * other.x - self.x * other.z,
                        self.x * other.y - self.y * other.x)


v1 = Vector3D(4, 1, 2)
v1.display()
v2 = Vector3D()
v2.read()
v3 = Vector3D(1, 2, 3)
v4 = v1 + v2
v4.display()
a = v4 * v3
print(a)
v4 = v1 * 10
v4.display()
v4 = v1 @ v3
v4.display()