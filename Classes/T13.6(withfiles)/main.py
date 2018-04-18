from Polynomial import Polynomial
import re
import os


def read_from_folder(folder_name):
    input_names = []
    polynomials_list = []
    for root, dirs, files in os.walk(folder_name):
        input_names.extend(files)
    for filename in input_names:
        if filename.endswith('.in'):
            p = Polynomial()
            p.read_from_file(folder_name, filename)
            polynomials_list.append(p)
    return polynomials_list


input_folder = 'in/'
P = read_from_folder(input_folder)
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
print((P[0] * P[1] - P[1]).display())