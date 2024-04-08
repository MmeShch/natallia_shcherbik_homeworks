#1.	Используя стандартные арифметические операции представьте самое большое целое число из цифр 4, 4, 4 и
#приведите его значение

#1)
number1 = 4 * 4 * 4
number2 = 4 ** 4 ** 4
number3 = 4 + 4 + 4
number4 = 4 - 4 - 4
number5 = 4 / 4 / 4
print(f'The largest integer after arithmetic operations\n'
      f' with 3 digits "4": {max(number1, number2, number3, number4, number5)}')

#2)
number = str('4') * 3
print(f'The largest integer is {int(number)}')

# 2. Написать программу для вычисления значения выражений. Проверить правильность выполнения задания с помощью
# # тестовых значений. y = 1/4*[sin(α+β-γ)+syn(β+γ-α)+syn(γ+α-β)-syn(α+β+γ)]
import math

a = int(input('Enter the angle α: '))
b = int(input('Enter the angle β: '))
y = int(input('Enter the angle γ: '))
x = 1/4 * (math.sin(a+b-y) + math.sin(b+y-a) + math.sin(y+a-b) - math.sin(a+b+y))
print(x)

#3.	Создать пустую переменную. Проверить ее на истинность и ложность. Объясните полученный результат.

var = None
print(bool(var)) # если перевести пустую переменную в логический тип данных, то она вернет значение False

# 4.В строке “Иван Иванов” поменяйте местами слова. Может быть предоставлена любая строка с именем и фамилией.
# например “Петр Иванов” => “Иванов Петр”

name_str = input('Enter the last name and the first name: ').split()
name_str.reverse()
print(' '.join(name_str))

# 5.Создать список с числами от 1 до 50 используя генератор списков.

lst = [x for x in range(1, 51)]
print(f'New list with digits from 1 to 50:\n{lst}')

# 6.Вам передан массив чисел. Известно, что каждое число в этом массиве имеет пару, кроме одного:
# [1, 5, 2, 9, 2, 9, 1] => 5

data = [1, 5, 2, 9, 2, 9, 1]
for i in set(data):
    if data.count(i) == 1:
        print(f'{i} has no pair in the list {data}')

# 7.Дан список [student1, student2, student3] с помощью цикла for добавить к каждому элементу списка слово “_good”.
# Вывести на экран.

data = ['student1', 'student2', 'student3']
data2 = [i + '_good' for i in data]
print(f'New list with new word is {data2}')

# 8. Вывести на экран числа от 0 до 50, кроме 35.

numbers = [i for i in range(0, 51)]
print(numbers, numbers.remove(35))

# 9.Дана строка [“hello my friend”, “my name is”, “house”, “cat”, “dog”]. В новый список добавить элементы,
# которые содержат пробел.

data = ['hello my friend', 'my name is', 'house', 'cat', 'dog']
new_data = []
for element in data:
    if ' ' in element:
        new_data.append(element)
print(new_data)

# 10. В классе N школьников. На уроке физкультуры тренер говорит «на первый-второй рассчитайтесь». Выведите, что скажут
# ученики. Входные данные: Вводится одно целое число — количество человек в классе. Входные данные: Выведите
# последовательность чисел 1 и 2, в том порядке, как будут говорить школьники.

num_pupils = int(input('Enter the number of pupils: '))
lst = [0] * num_pupils
for i in range(len(lst)):
    if i % 2 == 0:
        lst[i] = 1
    else:
        lst[i] = 2
print(*lst)

# 11. Дан список чисел, необходимо удалить все вхождения числа 20 из него.

numbers = [35, 18, 20, 48, 20, 98, 20, 14]
for num in numbers:
    if num == 20:
        numbers.remove(num)
print(f'New list without digit 20 is {numbers}')

# 12. С клавиатуры вводится десятизначное число. Вывести на экран четные числа входящие в данное число.
# Например 1234567892  2 4 6 7 8 2

num = int(input('Enter a 10-digit number: '))
lst = [int(i) for i in str(num)]
lst2 = []
for i in lst:
    if i % 2 == 0:
        lst2.append(i)
print(*lst2)

# 13. Необходимо удалить пустые строки из списка строк. Пример списка:
# [‘1’, ‘2’,  ‘3’ , ‘4’ ,’hello’, ‘’, ‘good’ , ‘’, ‘’, ‘5’, ‘6’, ‘7’]

str_list = ['1', '2', '3', '4', 'hello', '', 'good', '', '', '5', '6', '7']
str_list = [i for i in str_list if i != '']
print(f'The list without empty strings is {str_list}')

# 14. Напишите программу, которая принимает текст и выводит два слова: наиболее часто встречающееся и самое длинное.

text = """When I look back on that time now, I think of it as a hard-earned lesson about the importance of tenacity
and perseverance, but also about the need to steer clear of anger and anxiety over things you can’t control."""
print(text)
words = text.lower().split()
longest_word = max(words, key=len).strip(',').strip('.')
most_frequent = max(set(words), key=words.count)
print(f'The longest word in text - {longest_word}\nThe most frequent word in text - {most_frequent}')

# 15.Напишите программу, которая вычисляет процентное содержание символов G (гуанин) и C (цитозин) в введенной строке
# (программа не должна зависеть от регистра вводимых символов). Например, в строке "acggtgttat" процентное содержание
# символов G и C равно 4/10 ⋅ 100 = 40.0 где 4 - это количество символов G и C, а 10 -- это длина строки.

new_string = input('Enter a string with random quantity of "g" and "c": ').lower()
quantity = 0
for i in new_string:
    if i == 'c' or i == 'g':
        quantity += 1
percentage = quantity / len(new_string) * 100
print(f'Symbol percentage of "G" and "C" in string is {percentage}')

# 16. Дезоксирибонуклеиновая кислота (ДНК) представляет собой химическое вещество, находящееся в ядре клеток и несущее
# «инструкции» по развитию и функционированию живых организмов. В цепочках ДНК символы «А» и «Т» дополняют друг друга,
# как «С» и «G». Вам нужно вернуть другую дополнительную сторону. Нить ДНК никогда не бывает пустой или ДНК вообще
# не существует. Пример: (ввод --> вывод) “АТТGС" --> "ТААСG" “GТАТ" --> "САТА"

dna = input('Enter DNA: ').upper()
dict_dna = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
other_side_dna = ''.join(map(dict_dna.get, dna))
print(other_side_dna)