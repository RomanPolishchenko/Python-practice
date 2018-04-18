class Person:
    def __init__(self):
        self.surname = None
        self.b_year = None
        Person._count += 1

    def input(self):
        self.surname = input('Прізвище: ')
        self.b_year = int(input('Рік народження: '))

    def display(self):
        print(self.surname, self.b_year, end=' ')

    _count = 0

    def show_count():
        return Person._count

    show_count = staticmethod(show_count)
