#  3) Экземпляру класса при инициализации передается аргумент – список тем для разговора. Класс реализует методы:
# – add_theme(value) – добавить тему в конец;
# # – shift_one() – сдвинуть темы на одну вправо (последняя становится первой, остальные сдвигаются);
# # – reverse_order() – поменять порядок тем на обратный;
# # – get_themes() – возвращает список тем;
# # – get_first() – возвращает первую тему.
# Пример 1 Ввод:
# tl = Themes(['weather', 'rain'])
# tl.add_theme('warm')
# print(tl.get_themes())
# tl.shift_one()
# print(tl.get_first())
# Вывод:
# ('weather', 'rain', 'warm')
# warm

# class Themes:
#     def __init__(self, topics):
#         self.topics = topics
#
#     def add_theme(self, value):
#         self.topics.append(value)
#
#     def shift_one(self):
#         self.topics = [self.topics[-1]] + [self.topics[:-1]]
#
#     def reverse_order(self):
#         self.topics = self.topics[::-1]
#
#     def get_themes(self):
#         return tuple(self.topics)
#
#     def get_first(self):
#         return self.topics[0]
#
#
# tl = Themes(['weather', 'rain'])
# tl.add_theme('warm')
# print(tl.get_themes())
# tl.shift_one()
# print(tl.get_first())