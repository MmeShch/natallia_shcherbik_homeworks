# 2) Создайте класс Робот
#     создайте 2 типа оружия: меч, автомат
#     Создайте 2 типа амуниции: броня, шлем
#     Добавьте оружию и амуниции свои характеристики(например урон, прочность)
#     Создайте своего робота с каким либо оружием
#     (может быть несколько и брони может быть несколько. Так же может быть ничего)
#     Выведите весь арсенал робота на экран

class Robot:

    def __init__(self, name, weapon, ammunition):
        self.name = name
        self.weapon = weapon
        self.ammunition = ammunition


class Weapon:

    def __init__(self, name, damage, durability):
        self.name = name
        self.damage = damage
        self.durability = durability

class Ammunition:

    def __init__(self, name, protection):
        self.name = name
        self.protection = protection


sword = Weapon('Sword', 10, 50)
assault_rifle = Weapon('Assualt rifle', 100, 200)
armor = Ammunition('Armor', 40)
helmet = Ammunition('Helmet', 50)
my_robot = Robot('Red-94', [sword, assault_rifle], [armor, helmet])
print(f"{my_robot.name}'s Arsenal:")
print("Weapons:")
for weapon in my_robot.weapon:
    print(f"{weapon.name} - Damage: {weapon.damage}, Durability: {weapon.durability}")
print("\nAmmunition:")
for ammo in my_robot.ammunition:
    print(f"{ammo.name} - Protection: {ammo.protection}")
