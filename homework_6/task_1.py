# 1) Казино. Компьютер генерирует числа от 1 до 10 и от 1 до двух соответственно.
# Цифры от 1 до 10 отвечают за номера, а от 1 до 2 за цвета(1-красный, 2-черный).
# Пользователю дается 5 попыток угадать номер и цвет(Пример. Вводим с клавиатуры: 3 красный)
# В случае неудачи, вывести на экран правильную комбинацию.

import random

num = random.randint(1, 10)
color = random.randint(1, 2)
def_colors = {1: 'red', 2: 'black'}
attempts = 0

while attempts < 5:
    guess_num = int(input('Guess number between 1 and 10: '))
    guess_color = input('Guess red or black: ')
    if guess_num == num and guess_color == def_colors[color]:
        print('Congratulations, you guessed!')
        break
    else:
        print(f'Nice try, but failed. You have {4 - attempts} tries left')
        attempts += 1
if attempts >= 5:
    print(f'You have run out of 5 attempts\nRight number is {num} and right color is {def_colors[color]}')







