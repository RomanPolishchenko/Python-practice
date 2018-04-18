from Polynomial import Polynomial
import pickle

if __name__ == '__main__':
    n = int(input('How much polynomials: '))
    for i in range(n):
        p = Polynomial()
        p.input()
        filename = 'P_{}.in'.format(p.number)
        f = open(filename, 'wb')
        pickle.dump(p, f)
        f.close()
