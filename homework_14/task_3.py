# 3) В текстовом файле посчитать количество строк, а также для каждой отдельной строки определить количество в ней
# символов.

with open('task1_for_lesson14.txt', 'r') as file:
    lines = file.readlines()
    print(f'Original lines - {lines}')
print(f'The sum of all strings - {len(lines)}')
for position, element in enumerate(lines):
    print(f"{position + 1} string has {len(element.strip())} chars")

