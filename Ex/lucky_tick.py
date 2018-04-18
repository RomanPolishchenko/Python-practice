from math import factorial


def c(n, k):
    x = factorial(n)/(factorial(k) * factorial(n-k))
    return x


res1 = 0

for i in range(28):
    res1 += c(i+2, 2)

print('res1 = {}'.format(res1))

res2 = 0
for a1 in range(10):
    for a2 in range(10):
        for a3 in range(10):
            res2 += c(a1+a2+a3+2, 2)

print('res2 = {}'.format(res2))

res3 = 0
for a1 in range(10):
    for a2 in range(10):
        for a3 in range(10):
            for a4 in range(10):
                for a5 in range(10):
                    for a6 in range(10):
                        if a1 + a2 + a3 == a4 + a5 + a6:
                            res3 += 1

print('Ans = {}'.format(res3))
