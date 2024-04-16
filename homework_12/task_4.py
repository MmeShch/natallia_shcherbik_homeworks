# 4) Простейший калькулятор с введёнными двумя числами вещественного типа. Ввод с клавиатуры:
# операции + - * / и два числа. Операции являются функциями. Обработать ошибку: "Деление на ноль"
# Ноль использовать в качестве завершения программы (сделать как отдельную операцию)

# def calculate(operator, n1, n2):
#     if operator == '+':
#         return n1 + n2
#     elif operator == '-':
#         return n1 - n2
#     elif operator == '*':
#         return n1 * n2
#     elif operator == '/' and n2 == 0:
#         return 'Zero division'
#     elif operator == '/' and n2 != 0:
#         return n1 / n2
#     elif operator == '0':
#         return 'Stop program'
#
#
# op = input('Enter an operator +, -, *, /: ')
# num1 = float(input('Enter a number: '))
# num2 = float(input('Enter a number: '))
# print(calculate(op, num1, num2))


def calculate():
    sign = input('Enter the math operation +, -, *, /: ')
    n1 = float(input('Enter a number: '))
    n2 = float(input('Enter a number: '))
    if sign == '+':
        print('{} + {} = '.format(n1, n2), n1 + n2)
    elif sign == '-':
        print('{} - {} = '.format(n1, n2), n1 - n2)
    elif sign == '*':
        print('{} * {} = '.format(n1, n2), n1 * n2)
    elif sign == '/' and n2 != 0:
        print('{} / {} = '.format(n1, n2), n1 / n2)
    elif sign == '/' and n2 == 0:
        print('Zero division!')


calculate()


def again():
    calc_again = input('Do you want to calculate again? Please type Y for YES or N for NO: ')
    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('See you later.')


again()

