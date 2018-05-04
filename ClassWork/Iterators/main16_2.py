n = int(input('n = '))

seq = range(n, 0, -1)

x = iter(seq)

try:
    while True:
        a = next(x)
        if a % 2 == 0:
            print(a)
except StopIteration:
    pass
