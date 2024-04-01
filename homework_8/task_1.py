# 1) Дан словарь, ключами которого являются имена студентов, а значениями - их оценки по математике.
# Напишите программу для вычисления средней оценки по математике для всех студентов.
names = ['Peter', 'Alan', 'Anya', 'Steve', 'Emmy', 'George']
grades = [3, 5, 10, 8, 7, 6]
students = dict(zip(names, grades))
print(students)
sum_of_grades = 0
for value in students.values():
    sum_of_grades += value
mean_score = sum_of_grades/len(students)
print(f'Mean score of grades for the all students is {mean_score}')


