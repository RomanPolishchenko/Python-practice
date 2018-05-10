class WordsOrder:
    def __init__(self, data):
        self._data = data.split()  # list of words
        self._output = self._data  # output words, changing by self methods
        self._index = -1  # current index
        self._stop_index = None  # stop index

    def _update_indexes(self):
        self._stop_index = len(self._output)
        self._index = -1

    def right_order(self):
        self._output = self._data
        self._update_indexes()

    def reversed_order(self):
        self._output = list(reversed(self._data))
        self._update_indexes()

    def len_growth(self):
        self._output = sorted(self._data, key=len)
        self._update_indexes()

    def len_decrease(self):
        self._output = list(reversed(sorted(self._data, key=len)))
        self._update_indexes()

    def only_symmetric(self):
        self._output = [item for item in self._data if item == item[::-1]]
        self._update_indexes()

    def __iter__(self):
        return self

    def __next__(self):
        self._index += 1
        if self._index == self._stop_index:
            raise StopIteration
        return self._output[self._index]


if __name__ == '__main__':
    words = WordsOrder('Hello I am Roma')
    words.len_growth()
    for i in words:
        print(i)
    words.len_decrease()
    for i in words:
        print(i)

    words.only_symmetric()
    for i in words:
        print(i)
