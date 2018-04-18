from Person import Person
from functools import namedtuple

Trip = namedtuple('Trip', ['date', 'distant'])


class Driver(Person):
    def __init__(self):
        super().__init__()
        self._fee = 0
        self._carrying_capacity = 0
        self._drives = []

    def input(self):
        super().input()
        self._fee = int(input('Плата за тоно-кілометр: '))
        self._carrying_capacity = int(input('Вантажопідйомність автомобіля: '))

    def add_trip(self, date, distant):
        self._drives.append(Trip(date, distant))

    def show_trips(self):
        print(self.surname, 'trips:')
        for t in self._drives:
            print(self._drives.index(t) + 1, '. ', t.date, ': ', t.distant, ' km', sep='')

    def display(self):
        super().display()
        print('{}$/km {} - max tonnage'.format(self._fee, self._carrying_capacity), end='')

    def trip_cost(self, dist):
        return self._fee * self._carrying_capacity * dist

    def entire_cost(self):
        _cost = 0
        for _trip in self._drives:
            _cost += self._fee * self._carrying_capacity * _trip.distant
        return _cost


d = Driver()
d.input()
d.add_trip('12-13-2000', 123)
d.add_trip('23-01-1999', 45)
# d.show_trips()
print(d.entire_cost(), '$', sep='')
