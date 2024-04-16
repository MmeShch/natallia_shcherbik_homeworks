# 1)Создайте функцию для определения наибольшего числа

def find_max(x, y, z):
    return max(x, y, z)


a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
c = int(input('Enter the third number: '))
print(find_max(a, b, c))


# 2 способ:

def find_largest(a,b,c):
    if a > b and a > c:
        print(f'{a} is greatest')
    elif b > a and b > c:
        print(f'{b} is greatest')
    else:
        print(f'{c} is greatest')


find_largest(1000, 500, 18)






