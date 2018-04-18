import queue
from random import randint


def log(_filename, _action):
    f = open(_filename, 'a', encoding='utf-8')
    f.write(_action)
    f.write('\n')
    f.close()


def create_log_file(_filename):
    f = open(_filename, 'w', encoding='utf-8')
    f.close()


q = queue.Queue()

m = int(input('Amount of people: '))
t1 = int(input('Max time for serving: '))
t2 = int(input('Max time to add new customer: '))
T = int(input('Period of time: '))

for i in range(1, m + 1):
    q.put(i)

put_tick = randint(1, t2)
get_tick = randint(1, t1)

filename = 'logging.txt'
create_log_file(filename)

for i in range(1, T + 1):
    something_happen = False
    if put_tick == 0:
        put_tick = randint(1, t2)
        m += 1
        q.put(m)
        log(filename, 'At the moment {} {}-th customer was added.'.format(i, m))
        something_happen = True
    else:
        put_tick -= 1

    if get_tick == 0:
        get_tick = randint(1, t1)
        j = q.get()
        log(filename, 'At the moment {} {}-th customer was served.'.format(i, j))
        something_happen = True
    else:
        get_tick -= 1
    if not something_happen:
        log(filename, 'At the moment {} nothing happened'.format(i))

print(q.queue)
