# 6) Создать произвольный словарь 2. Добавить новый элемент с ключом типа str и значениемтипа int 3. Добавить новый
# элемент с ключом типа кортеж(tuple) и значением типа список(list) 4. Получить элемент по ключу 5. Удалить элемент
# по ключу 6. Получить список ключей словаряльности дубликаты

my_dict = {'age': 90,
           'occupation': 'retired',
           'fortune': 100000
}
my_dict.update(height=5.6)
print(my_dict)
my_dict[('cat', 'dog')] = [2, 1]
print(my_dict)
print(my_dict.get('age'))
print(my_dict.pop('fortune'))
print(list(my_dict.keys()))
