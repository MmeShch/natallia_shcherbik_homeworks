#2) Вы идете в путешествие, надо подсчитать сколько у денег у каждого студента.
# Класс студен описан следующим образом:
# class Student:
#     def __init__(self, name, money):
#        self.name = name
#        self.money = money

class Student:

    def __init__(self, name : str, money: float):
        self.name = name
        self.money = money


student1 = Student('Mike', 10)
student2 = Student('Alice', 15)
student3 = Student('Kate', 100)
student4 = Student('Tom', 19)

for student in (student1, student2, student3, student4):
    print(f'Student {student.name} has {student.money} money')

