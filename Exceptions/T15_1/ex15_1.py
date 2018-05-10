class WrongFormat(Exception):
    def __init__(self, num, base):
        self._num = num
        self._base = base

    def __str__(self):
        return "Wrong format. The {} can't be represented in base {}".format(self._num, self._base)


class WrongBase(Exception):
    def __init__(self, base):
        self._base = base

    def __str__(self):
        return 'Incorrect base: {}'.format(self._base)
