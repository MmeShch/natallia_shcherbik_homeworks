# 1) Файл содержит числа и буквы. Каждый записан в отдельной строке. Нужно считать содержимое в список
# так, чтобы сначала шли числа по возрастанию, а потом слова по возрастанию их длины.

with open('task1_for_lesson14.txt', 'r') as file:
    new_list = [i.replace('\n', '') for i in file.readlines()]
    print(f'Original list - {new_list}')
    numbers = []
    words = []
    for item in new_list:
        if item.isdigit():
            numbers.append(int(item))
        elif item.isalpha():
            words.append(item)
    numbers.sort()
    words.sort(key=len)
    print(f'New list - {numbers + words}')












