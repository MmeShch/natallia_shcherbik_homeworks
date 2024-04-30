# 1) Реализовать калькулятор с 4 методами: Сумма, вычитание , умножение, деление. Метод принимает 2 аргумента и
# возвращает результат. Невалидные данные должны быть обработаны(в классе написать проверку на валидность данных)

class Calculator:


    def is_valid_input(self, num1, num2):
        try:
            float(num1)
            float(num2)
            return True
        except ValueError:
            return False

    def get_sum(self, num1, num2):
        if self.is_valid_input(num1, num2):
            return float(num1) + float(num2)
        else:
            return 'Invalid input'

    def get_subtract(self, num1, num2):
        if self.is_valid_input(num1, num2):
            return float(num1) - float(num2)
        else:
            return 'Invalid input'

    def get_multiplication(self, num1, num2):
        if self.is_valid_input(num1, num2):
            return float(num1) * float(num2)
        else:
            return 'Invalid input'

    def get_division(self, num1, num2):
        if self.is_valid_input(num1, num2):
            if float(num2) != 0:
                return float(num1) / float(num2)
            else:
                return 'Division by zero!'
        else:
            return 'Invalid input'


calculate = Calculator()
while True:
    operator = input('Enter +, -, *, / or stop: ')
    if operator == 'stop':
        break
    if operator not in ('+', '-', '*', '/'):
        print('Wrong operator, try again')
        continue

    num1 = input('Enter 1st number: ')
    num2 = input('Enter 2nd number: ')

    if operator == '+':
        print(calculate.get_sum(num1, num2))
    elif operator == '-':
        print(calculate.get_subtract(num1, num2))
    elif operator == '*':
        print(calculate.get_multiplication(num1, num2))
    elif operator == '/':
        print(calculate.get_division(num1, num2))





