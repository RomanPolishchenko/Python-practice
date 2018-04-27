class Person:
    def __init__(self):
        self.name = None
        self.byear = None

    def input(self):
        self.name = input('Name: ')
        self.byear = input("B year:")

    def print(self):
        print(self.name, self.byear, end='')


class Employee(Person):
    def __init__(self):
        super().__init__()
        self.tab_num = None
        self.subdiv = None
        self.salary = None
        self.pos = None

    def input(self):
        super().input()
        self.tab_num = int(input('Tab num:'))
        self.subdiv = input('Subdiv:')
        self.pos = input('Pos:')
        self.salary = int(input("Salary:"))

    def print(self):
        super().print()
        print(self.tab_num, self.subdiv, self.salary, self.pos, end='')

    def readfile(self, line):
        line = line.split(', ')
        self.name = line[0]
        self.byear = int(line[1])
        self.tab_num = int(line[2])
        self.subdiv = line[3]
        self.pos = line[4]
        self.salary = int(line[5])

    def salary_year(self):
        return self.salary * 12


class Subdiv:
    def __init__(self, sname):
        self.sname = sname
        self.workers = []

    def add_employee(self, obj):
        self.workers.append(obj)

    def del_employee(self, obj):
        if obj in self.workers:
            self.workers.remove(obj)

    def ysalary(self):
        _ys = 0
        for worker in self.workers:
            _ys += worker.salary_year()
        return _ys


if __name__ == "__main__":
    filename = input('Filename:')
    subdivs = {}
    f = open(filename, 'r', encoding='utf-8')
    for line in f.readlines():
        emp = Employee()
        emp.readfile(line)
        if emp.subdiv in subdivs:
            subdivs[emp.subdiv].add_employee(emp)
        else:
            subdivs[emp.subdiv] = Subdiv(emp.subdiv)
            subdivs[emp.subdiv].add_employee(emp)

    for div, obj in subdivs.items():
        print('Subdiv {} - {}'.format(div, obj.ysalary()))
