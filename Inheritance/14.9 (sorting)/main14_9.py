from collections import deque

sequence = deque()

numbers = list(input('Enter your numbers: ').split())
for i in range(len(numbers)):
    sequence.appendleft(max(numbers))
    numbers.remove(max(numbers))

print('Sorted:', " ".join(sequence))
