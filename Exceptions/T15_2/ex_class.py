class WrongArgument(Exception):
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return 'Wrong argument: {}'.format(self._arg)
