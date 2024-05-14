# 1) Реализовать паттерн Singleton, чтобы был создан только первый экземпляр класса
# 2)
# Исходные данные:
# - скрипт task1, который содержит реализацию классов Car, CarCommander, CarGunner и
# код для проверки результата
# Необходимо:
# 1. Реализовать всю необходимую логику так, чтобы скрипт task1 выводил:
#     >>> Well done. Amazing job!
# Желательно:
# 1. Привести альтернативные способы решения задачи.
# Примечание:
# - НЕЛЬЗЯ менять реализацию приведенных в исходных данных классов и проверочного кода.
# - Нет ограничений по реализации классов CarMan и Vehicle, а также вспомогательной логики.

# 1st way

# class Singleton:
#     __instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls.__instance is None:
#             cls.__instance = super().__new__(cls)
#         return cls.__instance
#
#
# class Car(Singleton):
#     def __init__(self):
#         self.id = 1
#
#
# class CarCommander(Singleton):
#     def __init__(self):
#         self.id = 2
#
#
# class CarGunner(Singleton):
#     def __init__(self):
#          self.id = 3
#
#
# class CarMan(Singleton):
#     def __init__(self):
#         self.id = 4
#
#
# class Vehicle(Singleton):
#     def __init__(self):
#         self.id = 5
#
# def check_object_id_collector():
#     expected_ids = (1, 2, 3, 4, 5)
#     actual_ids = (Car().id, CarCommander().id, CarGunner().id, CarMan().id, Vehicle().id)
#     assert actual_ids == expected_ids, 'Expected_ids: {}. Actual_ids: {}.'.format(expected_ids, actual_ids)
#     print('Well done. Amazing job!')
#
#
# check_object_id_collector()


# 2nd way

def singleton(cls):
    instances = {}

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper

@singleton
class Car:
    def __init__(self):
        self.id = 1

@singleton
class CarCommander:
    def __init__(self):
        self.id = 2

@singleton
class CarGunner:
    def __init__(self):
         self.id = 3

@singleton
class CarMan:
    def __init__(self):
        self.id = 4

@singleton
class Vehicle:
    def __init__(self):
        self.id = 5

def check_object_id_collector():
    expected_ids = (1, 2, 3, 4, 5)
    actual_ids = (Car().id, CarCommander().id, CarGunner().id, CarMan().id, Vehicle().id)
    assert actual_ids == expected_ids, 'Expected_ids: {}. Actual_ids: {}.'.format(expected_ids, actual_ids)
    print('Well done. Amazing job!')


check_object_id_collector()