# 6) Простейший калькулятор c введёнными двумя числами вещественного типа. Ввод с клавиатуры: операции + - * / и
# два числа. Обработать ошибку: “Деление на ноль” Ноль использовать в качестве завершения программы
# (сделать как отдельную операцию).

while True:
    operator = input('Enter the operator (+, -, *, /, **, //, %): ')
    if operator == '0':
        break
    if operator in ('+, -, *, /, **, //, %'):
        n1 = float(input('Enter the number: '))
        n2 = float(input('Enter the number: '))
        if operator == '+':
            print(n1 + n2)
        elif operator == '-':
            print(n1 - n2)
        elif operator == '*':
            print(n1 * n2)
        elif operator == '/':
            if n2 == 0:
                print('You can not divide by zero!')
                break
            else:
                print(n1 / n2)
        elif operator == '**':
            print(n1 ** n2)
        elif operator == '//':
            if n2 == 0:
                print('You can not divide by zero!')
                break
            else:
                print(n1 // n2)
        elif operator == '%':
            if n2 == 0:
                print('You can not divide by zero!')
                break
            else:
                print(n1 % n2)
    else:
        print('Wrong sign, try again!')