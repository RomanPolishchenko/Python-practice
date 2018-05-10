import ex15_1

if __name__ == '__main__':
    num = input('Enter the number: ')
    base = input("Enter the base: ")
    try:
        base = int(base)
    except ValueError:
        raise ex15_1.WrongBase(base)

    try:
        num = int(num, base)
    except ValueError:
        raise ex15_1.WrongFormat(num, base)

    print("It's {} in decimal.".format(num))
