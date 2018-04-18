def read_code(filename):
    f = open(filename, 'r')
    _text = f.readlines()
    for _i in range(len(_text)):
        _text[_i] = _text[_i].rstrip()
    f.close()
    return _text


def beginning_spaces(string):
    _count = 0
    for _i in string:
        if _i == ' ':
            _count += 1
        else:
            break
    return _count


def error(row):
    # raise SyntaxError('Неверная табуляция в строке номер: ' + str(row))
    print('Wrong tabulation at line ' + str(row))


def opened_scopes_round(string):
    _count = 0
    for _i in string:
        if _i is '(':
            _count += 1
        elif _i is ')':
            _count += -1


def opened_scopes(string):
    _count_sq = 0
    _count_fig = 0
    for _i in string:
        if _i is '[':
            _count_sq += 1
        elif _i is ']':
            _count_sq += -1
        if _i is '{':
            _count_fig += 1
        elif _i is '}':
            _count_fig += -1
    return _count_sq, _count_fig


if __name__ == "__main__":
    text = read_code('input.txt')
    flag = True
    for i in range(len(text)):
        if beginning_spaces(text[i]) % 4 != 0:
            # if beginning_spaces(text[i]) % 4 == 1
            error(i + 1)
            flag = False
            break
        if text[i].endswith(':') and\
                (i == len(text)-1 or beginning_spaces(text[i])+4 != beginning_spaces(text[i+1])):
            error(i + 2)
            flag = False
            break
        if i == 0:
            if beginning_spaces(text[i]) != 0:
                error(i + 1)
                flag = False
                break
        else:
            if beginning_spaces(text[i]) > beginning_spaces(text[i-1]) and\
                    (not text[i-1].endswith(':') or not text[i-1].endswith('\\')):
                error(i + 1)
                flag = False
                break
    if flag:
        print("Correct tabulation!")
