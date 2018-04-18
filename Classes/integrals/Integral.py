class Integral:
    def __init__(self, func, a, b):
        self._func = func
        self._a = a
        self._b = b
        self._n = 10000
        self._h = (b - a)/self._n

    def set_intervals(self, n):
        self._n = n
        self._h = (self._b-self._a)/n

    def get_intervals(self):
        return self._n

    def _x(self, i):
        return self._a + i * self._h

    def left_rect(self):
        _int = 0
        for i in range(self._n):
            _int += self._func(self._x(i))*(self._x(i+1) - self._x(i))
        return _int

    def right_rect(self):
        _int = 0
        for i in range(1, self._n + 1):
            _int += self._func(self._x(i))*(self._x(i) - self._x(i-1))
        return _int

    def center_rect(self):
        _int = 0
        for i in range(1, self._n + 1):
            _int += self._func((self._x(i) + self._x(i+1))/2)*(self._x(i) - self._x(i-1))
        return _int

    def trapezium(self):
        _int = 0
        for i in range(1, self._n):
            _int += self._func(self._x(i))
        _int = self._h * ((self._func(self._x(0)) + self._func(self._x(self._n)))/2 + _int)
        return _int
