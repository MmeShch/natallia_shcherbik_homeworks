# 2) Экземпляр класса инициализируется с аргументом name – именем котенка. Класс реализует методы:
# – to_answer() – ответить: котенок через один раз отвечает да или нет, начинает с да. Метод возвращает “moore-moore”,
# если да, “meow-meow”, если нет. Одновременно увеличивается количество соответствующих ответов;
# – number_yes() – количество ответов да;
# – number_no() – количество ответов нет.
# Пример 1
# Ввод:
# tk = Talking('Pussy')
# print(tk.to_answer())
# print(tk.to_answer())
# print(tk.to_answer())
# print(f'{tk.name} says "yes" {tk.number_yes()} times, "no" {tk.number_no()} times')
# Вывод:
# moore-moore
# meow-meow
# moore-moore
# Pussy says "yes" 2 times, "no" 1 times

# class Kitten:
#     def __init__(self, name):
#         self.name = name
#         self.answers = []
#
#     def to_answer(self):
#         if len(self.answers) % 2 == 0:
#             self.answers.append('Yes')
#             return 'moore-moore'
#         else:
#             self.answers.append('No')
#             return 'meow-meow'
#
#     def number_yes(self):
#         return self.answers.count('Yes')
#
#     def number_no(self):
#         return self.answers.count('No')
#
#
# kitten = Kitten('Pussy')
# print(kitten.to_answer())
# print(kitten.to_answer())
# print(kitten.to_answer())
# print(f'{kitten.name} says "Yes" {kitten.number_yes()} times and "No" {kitten.number_no()} times ')
