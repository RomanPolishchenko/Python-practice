import multiarray


if __name__ == '__main__':
    s1 = input('String 1: ')
    s2 = input('String 2: ')
    s1 = multiarray.MultiArray(s1)
    s2 = multiarray.MultiArray(s2)

    if s1 == s2:
        flag_a = True
    else:
        flag_a = False

    if s1 <= s2:
        flag_b = True
    else:
        flag_b = False

    print('a) {}\nb) {}'.format(flag_a, flag_b))
