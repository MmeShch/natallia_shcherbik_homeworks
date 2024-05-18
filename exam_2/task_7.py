import datetime

class Person:
    def __init__(self, surname, birthdate):
        self.surname = surname
        self.birthdate = datetime.datetime.strptime(birthdate, '%Y-%m-%d').date()

    def calculate_age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
        return age

    def output_information(self):
        return f"Surname: {self.surname}, Date of Birth: {self.birthdate}, Age: {self.calculate_age()}"

class Applicant(Person):
    def __init__(self, surname, birthdate, faculty):
        super().__init__(surname, birthdate)
        self.faculty = faculty

    def output_information(self):
        return f"{super().output_information()}, Faculty: {self.faculty}"

class Student(Applicant):
    def __init__(self, surname, birthdate, faculty, course):
        super().__init__(surname, birthdate, faculty)
        self.course = course

    def output_information(self):
        return f"{super().output_information()}, Course: {self.course}"

class Professor(Applicant):
    def __init__(self, surname, birthdate, faculty, position, seniority):
        super().__init__(surname, birthdate, faculty)
        self.position = position
        self.seniority = seniority

    def output_information(self):
        return f"{super().output_information()}, Position: {self.position}, Seniority: {self.seniority}"



persons = [
    Applicant("Doe", "1990-05-20", "Engineering"),
    Student("Smith", "1995-02-15", "Computer Science", 3),
    Professor("Johnson", "1985-10-10", "Mathematics", "Professor", 10)
]

for person in persons:
    print(person.output_information())
def search_persons_by_age(persons_list, min_age, max_age):
    result = [person for person in persons_list if min_age <= person.calculate_age() <= max_age]
    return result

min_age = 25
max_age = 35

result = search_persons_by_age(persons, min_age, max_age)
print(f"\nPersons aged between {min_age} and {max_age} years:")
for person in result:
    print(person.output_information())