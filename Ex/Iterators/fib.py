# def fibgen():
#     """Генератор-функція чисел Фібоначчі."""
#     a, b = 1, 1
#     while True:
#         yield b
#         a, b = b, a + b
#
#
# n = int(input('n=? '))
# fg = fibgen()
# print('Числа Фібоначчі (next)')
# for i in range(n):
#     print(i + 1, next(fg))
#
# print('Числа Фібоначчі (for ... in ...)')
# i = 0
# for x in fibgen():
#     i = i + 1
#     if i > n:
#         break
#     print(i, x)


def fibgen(n):
    """Генератор-функція чисел Фібоначчі до n."""
    i = 0
    a, b = 1, 1
    while True:
        i = i + 1
        if i > n:                   # якщо дійшли до n
            raise StopIteration     # зупиняємось
        yield b
        a, b = b, a + b


n = int(input('n=? '))

print('Числа Фібоначчі')

for i, x in enumerate(fibgen(n)):
    print(i + 1, x)
