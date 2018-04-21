"""
This program reads the schedule of the flights from the schedule.txt and interpreting it, printing a table.
Table updates every 3 minutes. Program finishes when all the flights is gone.
"""
from prettytable import PrettyTable
from collections import OrderedDict
from Classes_schedule import Race
from datetime import datetime
import time


def read_schedule(filename):
    f = open(filename, 'r', encoding='utf-8')
    _flights = OrderedDict()
    for info in f.readlines():
        _flight = Race(info)
        _flights[_flight.code] = _flight
    return _flights


def curr_time():
    """
    Returns current time.
    """
    _time = datetime.today()
    return 'Current time is {}'.format(_time.strftime('%H:%M:%S'))


def print_table(_flights):
    """
    Prints the table by the _flights schedule.
    """
    print(curr_time())
    table = PrettyTable(['Code', 'Route', 'Arrival', 'Departure', 'Status', 'Delay'])
    for fl in _flights.values():
        table.add_row([fl.code, fl.route, fl.arr_time, fl.dep_time, fl.get_status(), fl.delay])
    print(table)


def update_table(_flights):
    """
    Updates schedule, deletes "Gone" flights.
    """
    _del = []
    for fl in _flights.values():
        if fl.get_status() == "Gone":
            _del.append(fl.code)
    for i in _del:
        _flights.pop(i)


if __name__ == "__main__":

    flights = read_schedule('schedule.txt')

    while flights:
        update_table(flights)
        if flights:
            print_table(flights)
            time.sleep(30)

    print(curr_time())
    print('All flights are gone!')
