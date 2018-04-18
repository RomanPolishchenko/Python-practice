def read_books(args):
    _books = {}
    for name in args:
        f = open(name, 'r', encoding='utf-8')
        _books[name] = f.read()
    return _books


def count_indents(book):
    _count = 0
    while book.find('\n') != -1:
        _count += 1
        book = book[book.find('\n'):].lstrip()
    return _count


def get_indent(book, n):
    _count = 0
    _indent = ''
    while book.find('\n') != -1:
        _count += 1
        if _count == n:  # c Якщо знаходимо потрібний абзац, то збергігаємо всю книгу починаючи з нього
            _indent = book
        if _count == n + 1:  # c Обрізаємо все зайве
            _indent = _indent[:_indent.find('\n')]
        book = book[book.find('\n'):].lstrip()
    return _indent.rstrip()


def get_word(ind, n):
    birth_signs = """ '",.!?-:;–""" + chr(171) + chr(8212) + chr(187) + chr(8230)
    _word = -1
    _count = 0
    _curr_word = ''
    for sign in ind:
        if sign in birth_signs:
            if _count == n:  # c Якщо натрапили на розділовий знак, а попереднє слово є шуканим
                _word = _curr_word
                break
            _curr_word = ''
        if sign.isalnum():  # c Якщо знайшли букву або цифру, то додаємо її до поточного слова
            if _curr_word == '':  # c Якщо це перший знак поточного слова, то +1 до лічильника слів
                _count += 1
            _curr_word += sign
        if _count == n and sign == ind[-1]:  # c Якщо після останнього слова немає знаків, то зберігаємо це
            _word = _curr_word
    return _word


if __name__ == "__main__":
    # lief = '1\n\n2\n\n3\n\n4\n\n\n\n\n5\n\n'
    # print(get_indent(lief, 1))
    # df = 'Hello! My name is Roma, and i`m a teacher.'
    # print(get_word(df, 9))
    pass
