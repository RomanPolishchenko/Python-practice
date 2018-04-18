class Auto:
    def __init__(self, c, f, l):
        self._counter = c  # t сколько автомобиль проехал
        self.fuel = f  # t сколько есть топлива
        self._consumption_100 = l  # t расход топлива на 100 км

    def add_fuel(self, k):
        self.fuel += k

    def get_counter(self):
        return self._counter

    def set_counter(self, k):
        self._counter = k

    def print_data(self):
        print('Fuel -', self.fuel)
        print('Distance -', self.get_counter())

    def consumption_1(self):
        _cons = (1 + (self._counter//1000)/100) * self._consumption_100/100
        return _cons

    def trip_consumption(self, dist):
        _beginning_consumption = self.consumption_1()
        self.set_counter(self.get_counter() + dist)
        _ending_consumption = self.consumption_1()
        self.set_counter(self.get_counter() - dist)
        _consumption = (_beginning_consumption + _ending_consumption) / 2
        return _consumption

    def go(self, dist):
        _required_fuel = self.trip_consumption(dist) * dist
        if _required_fuel > self.fuel:
            print('Not enough fuel!')
        else:
            self.set_counter(self.get_counter() + dist)
            self.fuel = self.fuel - _required_fuel


class Truck(Auto):
    def __init__(self, num, c, f, l, cap):
        self._num = num  # t номер грузовика
        self._carrying_capacity = cap  # t максимальная грузоподъёмность
        self._load = 0  # t сколько груза есть сейчас
        super().__init__(c, f, l)

    def get_capacity(self):
        return self._carrying_capacity

    def get_num(self):
        return self._num

    def set_load(self, w):
        self._load = w

    def drop_load(self):
        self._load = 0

    def consumption_with_weight(self, weight=0):
        _cons = self.consumption_1()
        _percents = 1 + (weight / 1000 * 5) / 100
        return _cons * _percents

# t = Truck('1a', 0, 100, 10, 1700)
# print(t.consumption_1())
# print(t.consumption_with_weight(1500))
