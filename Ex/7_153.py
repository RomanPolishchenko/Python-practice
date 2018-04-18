

def search1(filename, char):
    """
    функция подсчета количества строк, первый символ которых равный заданному
    :param filename: имя файла
    :param char: символ
    :return: количетво
    """
    file = open(filename, 'r', encoding='utf-8')
    count = 0
    for line in file:     # считываем строчки файла и проверяем первые символы
        if line and line[0] == char:
            count += 1
    file.close()
    return count


def search2(filename, char):
    """
    функция подсчета количества строк, первый символ которых равный заданному
    :param filename: имя файла
    :param char: символ
    :return: количетво
    """
    file = open(filename, 'r', encoding='utf-8')
    count = 0
    for line in file:     # считываем строчки файла
        line = line.strip()   # убираем \n
        if line and line[-1] == char:  # проверяем непустая ли строка и последний символ
            count += 1

    file.close()
    return count


def search3(filename):
    """
    функция подсчета количества строк, первый и последний символы которых равны

    :param filename: имя
    :return: количество
    """
    file = open(filename, 'r', encoding='utf-8')
    count = 0
    for line in file:  # считываем строки файла
        line = line.strip('\n')    # убираем \n
        if line and line[0] == line[-1]:  # проверяем непустая ли строка и крайние символы
            count += 1
    file.close()
    return count


def search4(filename):
    """
    функция подсчета количества строк, состоящих из одинаковых символов

    :param filename: имя файла
    :return: количество
    """
    file = open(filename, 'r', encoding='utf-8')
    count = 0
    for line in file:   # считываем строки из файла
        line = line.strip('\n')    # убираем \n
        line = set(line)       # переводим строку в множество (убираются одинаковые символы)
        if len(line) == 1:  # если остался один символ - строка удовлетворяет условие задачи
            count += 1
    file.close()
    return count


if __name__ == '__main__':
    name = input("Введите имя файла: ")

    s = input('Введите символ: ')

    print("к-во строк, которые начинаются на '{}': {}".format(s, search1(name, s)))
    print("к-во строк, которые заканчиваются на '{}': {}".format(s, search2(name, s)))
    print("к-во строк, первый и последний символы которых одинаковые: {}".format(search3(name)))
    print("к-во строк состоящих из одинаковых символов : {}".format(search4(name)))
