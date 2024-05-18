class TriangleChecker:

    def __init__(self, a, b, c):
        if a > 0 and b > 0 and c > 0:
            self.a = a
            self.b = b
            self.c = c
        else:
            print("Negative numbers won't work")

    def is_triangle(self):
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            return "Yah, you can build a triangle"
        else:
            return "Sorry, you can't build a triangle out of this"



triangle = TriangleChecker(1, 5, 5)
print(triangle.is_triangle())
