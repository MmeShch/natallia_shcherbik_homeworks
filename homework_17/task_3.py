# 3) Создать 4 фрукта.
# Апельсин, яблоко, мандарин, банан
# У всех фруктов есть сорт, список витаминов, цена, имя
# У апельсина, мандарина, банана есть метод очистить
# У яблока метод порезать
# У банана есть характеристика: кол-во калия
# Создать 4 объекта фрукта и использовать все доступные методы и характеристики
# При вызове метода очистить, должно писаться имя фрукта
# Например:
# `apple = Apple("sort", [a,b,c], 120, "apple")`
# `apple.clear()`
# `>>"apple очищен"`

class Fruit:

    def __init__(self, name, fruit_type, price, list_vitamins):
        self.name = name
        self.fruit_type = fruit_type
        self.price = price
        self.list_vitamins = list_vitamins

    def peel(self):
        print(f'{self.name} is peeled')


class Apple(Fruit):

    def slice(self):
        print('Apple is sliced')


class Banana(Fruit):
    def __init__(self, name, fruit_type, vitamins, price, potassium_amount):
        super().__init__(name, fruit_type, vitamins, price)
        self.potassium_amount = potassium_amount

    def peel(self):
        print(f'{self.name} is peeled')


class Orange(Fruit):
    def peel(self):
        print(f"{self.name} is peeled")


class Tangerine(Fruit):
    def peel(self):
        print(f"{self.name} is peeled")


apple = Apple('Ranet', 'Apple', 1.50, ['C', 'P'])
orange = Orange('Navel', 'Orange', 2, ['C', 'K'])
tangerine = Tangerine('Clementine', 'Tangerine', 1.70, ['C', 'A'])
banana = Banana('Cavendish', 'Banana', ['C', 'K'], 0.20, 358)

apple.slice()
banana.peel()
orange.peel()
tangerine.peel()
print(f'{banana.name} has a {banana.potassium_amount} of potassium')