class Wizard:
    def __init__(self, name, rating, age):
        self.name = name
        self.rating = rating
        self.age = age

    def change_rating(self, value):
        if value > 0:
            self.rating = min(self.rating + value, 100)
            self.age = max(self.age - abs(value) // 10, 18)
        elif value < 0:
            self.rating = max(self.rating + value, 1)
            self.age = min(self.age + abs(value) // 10, 100)

    def __iadd__(self, string):
        self.rating += len(string)
        self.age = max(self.age - len(string) // 10, 18)
        return self

    def __call__(self, number):
        return (number - self.age) * self.rating

    def __str__(self):
        return f"Wizard {self.name} with {self.rating} rating looks {self.age} years old"

    def __lt__(self, other):
        if self.rating != other.rating:
            return self.rating < other.rating
        elif self.age != other.age:
            return self.age < other.age
        else:
            return self.name < other.name

    def __gt__(self, other):
        return not self.__lt__(other)

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

    def __eq__(self, other):
        return self.name == other.name and self.rating == other.rating and self.age == other.age

    def __ne__(self, other):
        return not self.__eq__(other)


wizard1 = Wizard("Gandalf", 80, 70)
wizard2 = Wizard("Saruman", 45, 65)

wizard1.change_rating(10)
print(wizard1)

wizard1 += "magic"
print(wizard1)

print(wizard1(100))

print(wizard1 > wizard2)