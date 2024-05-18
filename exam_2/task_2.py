# 2)
class Tomato:
    states = {
        0: 'Absent',
        1: 'Flowering',
        2: 'Green',
        3: 'Red'
    }

    def __init__(self, index):
        self._index = index
        self._state = self.states[0]

    def grow(self):
        if self._state != self.states[3]:
            current_index = list(self.states.keys())[list(self.states.values()).index(self._state)]
            self._state = self.states[current_index + 1]

    def is_ripe(self):
        return self._state == self.states[3]


class TomatoBush:
    def __init__(self, num_tomatoes):
        self.tomatoes = [Tomato(index) for index in range(1, num_tomatoes + 1)]


    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    def give_away_all(self):
        self.tomatoes = []


class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print("Harvested all ripe tomatoes!")
        else:
            print("Warning: Not all tomatoes are ripe yet.")

    @staticmethod
    def knowledge_base():
        print("Gardening Help: Remember to water and care for your plants regularly for healthy growth.")


Gardener.knowledge_base()
bush = TomatoBush(10)
gardener = Gardener('John', bush)
gardener.work()
gardener.harvest()
while not bush.all_are_ripe():
    gardener.work()
gardener.harvest()
