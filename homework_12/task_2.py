# 2) Создайте функцию для вывода таблицы умножения для указанного числа

def mult_table(number):
    for row in range(1, number + 1):
        for column in range(1, number + 1):
            print(row * column, end='\t')
        print()


inp_number = int(input('Enter a number: '))
mult_table(inp_number)