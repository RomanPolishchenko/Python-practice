class UkrainianChars:
    chars = 'йцукенгшщзхїґфівапролджєячсмитьбю'  # ukrainian alphabet

    def __init__(self, data):
        self._data = data
        self.sift()
        self._index = -1
        self._stop_index = len(self._data)

    def sift(self):
        _ch = []  # chars to delete
        for char in self._data:
            if char not in self.chars:
                _ch.append(char)
        for char in _ch:
            self._data = self._data.replace(char, '')

    def __iter__(self):
        return self

    def __next__(self):
        self._index += 1
        if self._index == self._stop_index:
            raise StopIteration
        return self._data[self._index]


if __name__ == '__main__':
    text = UkrainianChars('reqапортrt')
    for i in text:
        print(i)
