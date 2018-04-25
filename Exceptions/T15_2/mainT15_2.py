from ex_class import WrongArgument


def log(_arg, eps=10**-1):
    try:
        x = float(_arg)
        assert abs(x) < 1, WrongArgument(_arg)
        x_k = x
        x_k1 = -x**2/2
        y = x_k + x_k1
        i = 2
        while abs(x_k - x_k1) > eps:
            i += 1
            x_k, x_k1 = x_k1, (-1)**(i+1)*x**i/i
            y += x_k1
        return 'y = ln(1 + x) = {}'.format(y)
    except ValueError:
        raise WrongArgument(_arg)


if __name__ == '__main__':
    arg = input('x = ')
    print(log(arg))
