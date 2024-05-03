# 1) Создайте класс Students, содержащий поля:
# фамилия и инициалы, номер группы, успеваемость (список из пяти элементов).
# Создать класс School:
# Добавить возможность для добавления студентов в школу
# Добавить возможность вывода фамилий и номеров групп студентов, имеющих оценки, равные только 5 или 6.
# Добавить возможность вывода учеников заданной группы
# Добавить возможность вывода учеников претендующих на автомат(средний балл >= 7)

class Student:


    def __init__(self, lastname, initials, group_num, progress):
        self.lastname = lastname
        self.initials = initials
        self.group_num = group_num
        self.progress = progress


class School:


    def __init__(self):
        self.students = []

    def add_students(self, student):
        self.students.append(student)

    def students_with_grade_5_6(self):
        for student in self.students:
            if all(grade in [5, 6] for grade in student.progress):
                print(f'Last name: {student.lastname}, group: {student.group_num}')

    def students_in_group(self, group_num):
        for student in self.students:
            if student.group_num == group_num:
                print(f'Last name: {student.lastname}, group: {student.group_num}')

    def grade_point_average(self):
        for student in self.students:
            if (sum(student.progress) / len(student.progress)) >= 7:
                print(f'Last name: {student.lastname}, group: {student.group_num}')


school = School()

student1 = Student('Klinton', 'H.', 1, [5, 6, 7, 8, 8])
student2 = Student('Bush', 'J.', 2, [6, 7, 7, 8, 9])
student3 = Student('Obama', 'B.', 3, [8, 8, 9, 9, 8])

school.add_students(student1)
school.add_students(student2)
school.add_students(student3)

print('Students with grade 5 and 6: ')
school.students_with_grade_5_6()
print('Students of group 1: ')
school.students_in_group(1)
print('Students with grade point average >=7: ')
school.grade_point_average()




