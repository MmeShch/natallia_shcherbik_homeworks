# 7) Вася начал тренироваться бегать.В первый день день он пробежал 1 км. Каждый последующий день он увеличивал
# пройденное расстояние на 10% от предыдущего дня. Сколько дней Васе понадобится, чтобы пробежать в сумме хотя бы 10 км?

day = 0
distance = 1
dist_every_other_day = distance + (distance * 10 / 100)
while distance <= 10:
    distance += dist_every_other_day
    day += 1
print(f'Васе понадобиться {day} дней, чтобы пробежать в сумме хотя бы 10 км')



