from math import *
from Integral import Integral

int_1 = Integral(lambda x: sin(x) + x**2, 0, pi)
print('T – {}'.format(int_1.trapezium()))
