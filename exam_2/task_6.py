class Worker:
    def __init__(self, name, position, work_experience):
        self.name = name
        self.position = position
        self.work_experience = work_experience

    def print_info(self):
        if self.work_experience % 10 == 1 and self.work_experience % 100 != 11:
            years_str = "year"
        else:
            years_str = "years"
        print(f"Name: {self.name} Position: {self.position} Length of service: {self.work_experience} {years_str}")

# Example usage:
worker1 = Worker("Alexey", "Programmer", 17)
worker1.print_info()

worker2 = Worker("Anna", "Marketer", 2)
worker2.print_info()

worker3 = Worker("Dmitry", "Analyst", 1)
worker3.print_info()