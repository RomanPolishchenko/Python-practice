import queue
from random import randint


q = queue.Queue()
nums = input('Enter beginning numbers: ')
n = abs(int(input('Enter quantity of tests: ')))

for i in nums.split():
    q.put(int(i))

for i in range(n):
    inst = randint(0, 1)
    if inst:
        q.put(int(input('Got 1. Add a number: ')))
    else:
        print('Got 0. From queue got {}'.format(q.get()))

print('Queue size – {}'.format(q.qsize()))  # 10.2(a)
print('Queue – {}'.format(list(q.queue)))
print('Reversed queue – {}'.format(list(reversed(list(q.queue)))))  # 10.2(b)
