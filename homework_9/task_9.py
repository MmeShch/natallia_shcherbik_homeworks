# 9) Дана строка. Сохранить в ней только первые вхождения символов, удалив все остальные.
# Результат вывести в виде кортежа.

string1 = input('Enter a string: ').lower()
tuple1 = ()
for char in string1:
    tuple1 += (char[:1:],)
print(f'New tuple {tuple1}')


