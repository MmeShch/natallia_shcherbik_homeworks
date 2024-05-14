# Класс Bus содержит свойства: – speed (скорость), –capacity (максимальное количество пассажиров),– maxSpeed
# (максимальная скорость), – passengers (список имен пассажиров), – hasEmptySeats (наличие свободных мест),
#– seats (словарь мест в автобусе);
# методы:
# – посадка и высадка одного или нескольких пассажиров, – увеличение и уменьшение скорости на заданное значение.
# – операции "in", "+=" и "−=" (посадка и высадка пассажира(ов) с заданной фамилией)

class Bus:
    def __init__(self, speed, capacity, max_speed):
        self.speed = speed
        self.capacity = capacity
        self.max_speed = max_speed
        self.passengers = []
        self.has_empty_seats = True
        self.seats = {}


    def board(self, *passengers):
        for passenger in passengers:
            if len(self.passengers) < self.capacity:
                self.passengers.append(passenger)
                self.seats[passenger] = len(self.passengers)
            else:
                print(f'{passenger} cannot board. The bus is full.')
        self.has_empty_seats = len(self.passengers) < self.capacity


    def alight(self, *passengers):
        for passenger in passengers:
            if passenger in self.passengers:
                self.passengers.remove(passenger)
                del self.seats[passenger]
            else:
                print(f'{passenger} is not in the bus')
        self.has_empty_seats = len(self.passengers) < self.capacity

    def increase_speed(self, value):
        if self.speed + value <= self.max_speed:
            self.speed += value
            print(f'Speed has increased on {value} km/h and now is {self.speed} km/h')
        else:
            print('There is overspeeding')

    def decrease_speed(self, value):
        if self.speed - value >= 0:
            self.speed -= value
            print(f'Speed has decreased on {value} km/h and now is {self.speed} km/h')
        else:
            print('Speed cannot be lower than zero')


    def __contains__(self, passenger):
        return passenger in self.passengers

    def __iadd__(self, passenger):
        self.board(passenger)
        return self

    def __isub__(self, passenger):
        self.alight(passenger)
        return self


bus = Bus(speed=0, capacity=20, max_speed=120)
bus.board('Alice', 'Mike', 'Nick', 'John')
print(bus.passengers)
bus += 'David'
bus += 'Jim'
print('Passengers in the bus', bus.passengers)
bus -= 'Alice'
print('Passengers in the bus', bus.passengers)
bus.increase_speed(5)
bus.decrease_speed(10)



