# 2) Создать текстовый файл, записать в него построчно данные, которые вводит пользователь. Окончанием ввода
# пусть служит пустая строка.

with open('task2_for_lesson14.txt', 'w') as file:
    while True:
        data = input('Enter some data: ')
        if not data:
            break
        file.write(data + '\n')








