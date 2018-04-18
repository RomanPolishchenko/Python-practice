import pickle


def sign(x):
    if x > 0:
        _s = " + "
    else:
        _s = " - "
    return _s


class Polynomial:
    _count = 0

    def __init__(self):
        Polynomial._count += 1
        self.coefficients = {}
        self.number = Polynomial._count

    def input(self):
        print("P{}".format(self.number))
        n = int(input('Highest power: '))
        for i in range(n, -1, -1):
            a = int(input('a{} = '.format(i)))
            self.coefficients[i] = a

    def value_at(self, x):
        _result = 0
        for power, value in self.coefficients.items():
            _result += value*x**power
        return _result

    def derivative(self):
        _coe = {}
        for i in range(len(self.coefficients) - 2, -1, -1):
            _coe[i] = self.coefficients[i+1] * (i + 1)
        self.coefficients = _coe

    def __add__(self, other):
        _result = Polynomial()
        for i in range(max(len(self.coefficients), len(other.coefficients)) - 1, -1, -1):
            _result.coefficients[i] = self.coefficients.get(i, 0) + other.coefficients.get(i, 0)
        return _result

    def __sub__(self, other):
        _result = Polynomial()
        for i in range(max(len(self.coefficients), len(other.coefficients)) - 1, -1, -1):
            _result.coefficients[i] = self.coefficients.get(i, 0) - other.coefficients.get(i, 0)
        return _result

    def __mul__(self, other):
        _result = Polynomial()
        for i in range(len(self.coefficients) + len(other.coefficients) - 2, -1, -1):
            _result.coefficients[i] = 0

        for power_s, value_s in self.coefficients.items():
            for power_o, value_o in other.coefficients.items():
                _result.coefficients[power_s + power_o] += value_s * value_o
        return _result

    def display(self):
        _pol = ''
        for i, val in self.coefficients.items():
            if val != 0:
                if i == 0:
                    _pol += sign(val) + str(abs(val))
                elif i == 1:
                    _pol += sign(val) + '{}*x'.format(abs(val), i)
                else:
                    _pol += sign(val) + '{}*x^{}'.format(abs(val), i)
        if _pol[1] == '+':
            _pol = _pol[2:]
        if _pol[0] == ' ':
            _pol = _pol[1:]
        print('P{}: {}'.format(self.number, _pol))

    def read_from_file(self, directory, filename):
        f = open(directory + filename, 'rb')
        p = pickle.load(f)
        f.close()
        self.coefficients = p.coefficients
        self.number = p.number
