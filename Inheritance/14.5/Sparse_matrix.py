from collections import defaultdict
from copy import deepcopy


class Sparse:  # Sparse matrix
    def __init__(self, *args):
        self._elements = defaultdict(lambda: 0)
        self.m = 0
        self.n = 0
        self.parse(args)

    def parse(self, args):
        if len(args):  # if there is basic matrix
            _prototype = args[0]
            if isinstance(_prototype, list):  # if it's list
                matrix = _prototype
                self.m = len(matrix)
                self.n = len(matrix[0])
                for i in range(self.m):
                    for j in range(self.n):
                        if matrix[i][j]:
                            self._elements[(i, j)] = matrix[i][j]
            elif isinstance(_prototype, Sparse):
                self.m = _prototype.m
                self.n = _prototype.n
                self._elements = deepcopy(_prototype.get_elements())
            else:
                raise TypeError

    def get_elements(self):
        return self._elements

    def __str__(self):
        return str(dict(self._elements))

    def __add__(self, other):
        _sum = Sparse(self)
        if _sum.m == other.m and _sum.n == other.n:
            for key, value in other.get_elements().items():
                _sum.get_elements()[key] += other.get_elements()[key]
        else:
            raise ValueError
        return _sum


if __name__ == "__main__":

    mat1 = Sparse([[0, 0, 1], [0, 0, 0], [0, 2, 0]])
    mat2 = Sparse([[0, 0, 0], [0, 1, 0], [0, 0, 0]])

    # print(mat1 + mat2)
