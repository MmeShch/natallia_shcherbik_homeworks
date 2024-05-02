# 1) Файл "books.csv" содержит информацию о книгах в следующем формате:
#
# Название,Автор,Год издания,Жанр,Цена
# Мастер и Маргарита,Михаил Булгаков,1967,Фэнтези,500
# Преступление и наказание,Фёдор Достоевский,1866,Классика,400
# 1984,Джордж Оруэлл,1949,Научная фантастика,350
# Тень горы,Грегори Дэвид Робертс,2007,Триллер,600
#
# Реализовать функцию load_books(file_path), которая загружает данные из файла "books.csv"
# и возвращает список словарей, где каждый словарь представляет информацию о книге.
# Написать функцию total_price(books), которая принимает на вход список книг и
# возвращает общую стоимость всех книг.
# Создать функцию books_by_genre(books, genre), которая выводит на экран названия
# и авторов книг определенного жанра.
# Разработать скрипт, который загружает данные о книгах, вычисляет и выводит их
# общую стоимость, а также список книг определенного жанра, например, "Фэнтези".

import csv

book_data = [
    ["Master and Margarita", "Mikhail Bulgakov", 1967, "Fantasy", 500],
    ["Crime and Punishment", "Fyodor Dostoevsky", 1866, "Classic", 400],
    ["1984", "George Orwell", 1949, "Science Fiction", 350],
    ["Shadow of the Mountain", "Gregory David Roberts", 2007, "Thriller", 600]
]

with open('books.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Author", "Year of publication", "Genre", "Price"])
    writer.writerows(book_data)


def load_books(file_path):
    list_books = []
    with open('books.csv', 'r') as file:
        data = csv.DictReader(file)
        for elem in data:
            list_books.append(elem)
    return list_books



def total_price(books):
    total = 0
    for element in books:
        element['Price'] = int(element['Price'])
        total += element.get('Price', 0)
    return total



def books_by_genre(books, genre):
    for elem in books:
        if elem.get('Genre') == genre:
            print(f'Title: {elem.get("Title")}, Author: {elem.get("Author")}')


data_books = load_books('books.csv')
print(data_books)
print(f'Total price of books is {total_price(data_books)} ')
genre = input('Enter a genre of a book: ')
if genre.istitle() and genre in ['Fantasy', 'Classic', 'Science Fiction', 'Thriller']:
    print(f'Books of genre {genre}: ')
    books_by_genre(data_books, genre)
else:
    print('There are no books of such genre in list')








