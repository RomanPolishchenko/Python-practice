class ReversedNotEmpty:
    def __init__(self, data):
        self._data = data
        self.sift()
        self._index = len(data)

    def sift(self):
        _emp = []  # list of empty items
        for item in self._data:
            if not item:
                _emp.append(item)
        for item in _emp:
            self._data.remove(item)

    def __iter__(self):
        return self

    def __next__(self):
        if self._index == 0:
            raise StopIteration
        self._index -= 1
        return self._data[self._index]


if __name__ == '__main__':
    a = ReversedNotEmpty(['', 12, '2', [], None])
    for i in a:
        print(i)
