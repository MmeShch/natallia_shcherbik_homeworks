# 2) Класс «Прямоугольный треугольник»
# Класс содержит два действительных числа – стороны треугольника. и включает следующие методы:
# увеличение/уменьшение размера стороны на заданное количество процентов; вычисление радиуса описанной окружности,
# вычисление периметра, определение значений углов.
import math


class RightTriangle:

    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def increase(self, percent):
        self.side1 *= (1 + percent / 100)
        self.side2 *= (1 + percent / 100)


    def decrease(self, percent):
        self.side1 *= (1 - percent / 100)
        self.side2 *= (1 - percent / 100)

    def circumcircle_radius(self):
        return math.sqrt(self.side1 ** 2 + self.side2 ** 2) / 2


    def perimeter(self):
        return self.side1 + self.side2 + math.sqrt(self.side1 ** 2 + self.side2 ** 2)

    def angle_values(self):
        angle1 = 90
        angle2 = math.degrees(math.atan2(self.side2, self.side1))
        angle3 = math.degrees(math.atan2(self.side1, self.side2))
        return angle1, angle2, angle3


triangle = RightTriangle(5, 6)
triangle.increase(50)
print(f'New sides after increasing {triangle.side1}, {triangle.side2}')
triangle.decrease(20)
print(f'New sides after decreasing {triangle.side1}, {triangle.side2}')
print(f'Perimeter of triangle is {triangle.perimeter()}')
print(f'Raduis of circumcircle of triangle is {triangle.circumcircle_radius()}')
angle1, angle2, angle3 = triangle.angle_values()
print(f'The values of triangle angles: {angle1}, {angle2}, {angle3}')