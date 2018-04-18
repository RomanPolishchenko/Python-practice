from Person import Pal
import pickle


def create_book(file_name):
    """Creates the handbook in file "file_name".
    """
    f = open(file_name, 'wb')
    book = []
    n = int(input('Quantity of pals: '))
    for i in range(n):
        print('Pal {}'.format(i + 1))
        p = Pal()
        p.input()
        book.append(p)
    pickle.dump(book, f)
    f.close()


def add_pal(file_name):
    """Adds a new record in a file_name.
    """
    f = open(file_name, 'wb')
    book = pickle.load(f)
    p = Pal()
    p.input()
    book.append(p)
    pickle.dump(book, f)
    f.close()


def find_pal(file_name):
    """
    Looking for the number of the person with entered surname.
    :param file_name: name of handbook
    :return: number or denial.
    """
    surname = input('Whom are u looking for: ')
    f = open(file_name, 'rb')
    book = pickle.load(f)
    ans = "There is no person with such surname."
    for person in book:
        if person.surname == surname:
            ans = 'His/her number - ' + person.number
    f.close()
    return ans


def change_number(file_name):
    """
    Changes the number of entered person.
    :param file_name: file name
    :return: None
    """
    surname = input('Whose number are u gonna change: ')
    number = input("Enter a new number: ")
    f = open(file_name, 'rb')
    book = pickle.load(f)
    f.close()
    found = False
    for person in book:
        if person.surname == surname:
            found = True
            person.number = number
    if found:
        print('The number was successfully changed!')
    else:
        print("There is no person with such surname.")
    f = open(file_name, 'wb')
    pickle.dump(book, f)
    f.close()


def display(file_name):
    f = open(file_name, 'rb')
    book = pickle.load(f)
    print("Here is your handbook:")
    for i, pal in enumerate(book):
        print("{}. {} – {}".format(i + 1, pal.surname, pal.number))
    f.close()

if __name__ == "__main__":
    f_name = input('Enter the file name: ')
    create_book(f_name)
