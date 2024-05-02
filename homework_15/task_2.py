# 2) Создайте функцию, которая принимает на вход список словарей и сохраняет его в CSV файл.
# Каждый словарь представляет собой строку данных, а ключи словарей - названия столбцов.
import csv


def write_dicts_to_csv(dict_list, filename):
    keys = dict_list[0].keys()
    with open(filename, 'w', newline='') as file:
        dict_writer = csv.DictWriter(file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(dict_list)


list_of_films = [
    {'Studio': 'Disney', 'Film': 'Beauty and the Beast', 'Character': 'Belle'},
    {'Studio': 'Marvel', 'Film': 'Iron Man', 'Character': '"Tony" Stark'},
    {'Studio': 'Pixar', 'Film': 'Monsters, Inc.', 'Character': 'Mike Wazowski'}
]

write_dicts_to_csv(list_of_films, 'films.csv')


