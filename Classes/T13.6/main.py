from Polynomial import Polynomial
import re

n = int(input('How much polynomials: '))
P = []
for i in range(n):
    p = Polynomial()
    p.input()
    P.append(p)


exp = input('Enter your expression: ').replace(' ', '')
exp = re.split('(\W+)', exp)  # честно, просто загуглил, но хочу сам позже разобраться
for i in range(len(exp)):
    if len(exp[i]) == 2:
        exp[i] = P[int(exp[i][1]) - 1]


while '*' in exp:
    i = exp.index('*')
    exp = exp[:i-1] + [exp[i-1] * exp[i+1]] + exp[i+2:]
while '+' in exp:
    i = exp.index('+')
    exp = exp[:i-1] + [exp[i-1] + exp[i+1]] + exp[i+2:]
while '-' in exp:
    i = exp.index('-')
    exp = exp[:i-1] + [exp[i-1] - exp[i+1]] + exp[i+2:]

exp[0].display()
