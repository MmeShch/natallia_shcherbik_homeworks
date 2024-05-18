class Student:
    def __init__(self, name="Ivan", age=18, group_number="10A"):
        self.name = name
        self.age = age
        self.groupNumber = group_number

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_group_number(self):
        return self.group_number

    def set_name_age(self, name, age):
        self.name = name
        self.age = age

    def set_group_number(self, group_number):
        self.group_number = group_number


student1 = Student("John", 19, "11B")
student2 = Student("Alice", 20, "12C")
student3 = Student("Bob", 18, "10A")
student4 = Student("Eva", 21, "13D")
student5 = Student("Mike", 19, "11B")

print("Initial Data:")
print(f"Student1: {student1.get_name()}, {student1.get_age()}, {student1.get_group_number()}")
print(f"Student2: {student2.get_name()}, {student2.get_age()}, {student2.get_group_number()}")
print(f"Student3: {student3.get_name()}, {student3.get_age()}, {student3.get_group_number()}")
print(f"Student4: {student4.get_name()}, {student4.get_age()}, {student4.get_group_number()}")
print(f"Student5: {student5.get_name()}, {student5.get_age()}, {student5.get_group_number()}")

student1.set_name_age("John Doe", 20)
student3.set_group_number("12A")
student5.set_name_age("Mike Brown", 22)

print("\nUpdated Data:")
print(f"Student1: {student1.get_age()}, {student1.get_age()}, {student1.get_group_number()}")
print(f"Student2: {student2.get_name()}, {student2.get_age()}, {student2.get_group_number()}")
print(f"Student3: {student3.get_name()}, {student3.get_age()}, {student3.get_group_number()}")
print(f"Student4: {student4.get_name()}, {student4.get_age()}, {student4.get_group_number()}")
print(f"Student5: {student5.get_name()}, {student5.get_age()}, {student5.get_group_number()}")