# 4)На вход программы подается словарь a = {1:10, 2:20, 3:30},необходимо получить список произведения ключа на значение.

a = {1: 10, 2: 20, 3: 30}
print(f'Dictionary {a}')
lst = []
for key, value in a.items():
    lst.append(key * value)
print(f'New list {lst}')

