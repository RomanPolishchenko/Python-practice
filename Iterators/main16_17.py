"""
y = 1/(1+x)**3

"""


def y(_x):
    _i = 0
    while True:
        _y = (-1)**_i * (_i + 1)*(_i + 2)/2 * _x**_i
        yield _y
        _i += 1


if __name__ == '__main__':

    print('y = 1/(1+x)**3')
    x = float(input('|x| < 1: x = '))
    eps = float(input('Accuracy: eps = '))

    Sum = 0
    curr = 0

    for i in y(x):
        Sum += i
        if abs(curr - i) < eps:
            break
        curr = i
        # print(i)

    print('Got ', Sum)
    print('Calculated ', 1/(1+x)**3)
