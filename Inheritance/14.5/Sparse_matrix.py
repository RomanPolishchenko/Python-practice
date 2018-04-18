from collections import defaultdict
from copy import deepcopy


class Sparse:  # Sparse matrix
    def __init__(self, *args):
        self._elements = defaultdict(lambda: 0)
        self.m = 0
        self.n = 0
        self.parse(args)

    def parse(self, args):
        """
        Parsing matrix from args.
        """
        if len(args):  # if there is prototype
            _prototype = args[0]
            if isinstance(_prototype, list):  # if it's list
                matrix = _prototype
                self.m = len(matrix)
                self.n = len(matrix[0])
                for i in range(self.m):
                    for j in range(self.n):
                        if matrix[i][j]:
                            self._elements[(i, j)] = matrix[i][j]
            elif isinstance(_prototype, Sparse):  # if it's another matrix
                self.m = _prototype.m
                self.n = _prototype.n
                self._elements = deepcopy(_prototype.get_elements())
            else:
                raise Exception('Incorrect prototype')

    def get_elements(self):
        """
        Function returns elements dictionary.
        """
        return self._elements

    def get_elem(self, i, j):
        """
        Function returns (i, j)-th element of matrix.
        """
        return self._elements[(i, j)]

    def is_null(self, i, j):
        """
        Checks if (i, j)-th element is 0.
        """
        _flag = True
        if self._elements.get((i, j)):
            _flag = False
        return _flag

    def __str__(self):
        return str(dict(self._elements))

    def __add__(self, other):
        _sum = Sparse(self)
        if _sum.m == other.m and _sum.n == other.n:
            for key, value in other.get_elements().items():
                _sum.get_elements()[key] += other.get_elements()[key]
        else:
            raise Exception('Incorrect size of matrix')
        return _sum

    def __mul__(self, other):
        if self.n == other.m:

            def _get_factor(_mat1, _mat2, _i, _j):
                """
                Function gets (i, j)-th element of production mat1*mat2.
                """
                _elem = 0
                for _k in range(_mat1.n):
                    if not _mat1.is_null(_i, _k) and not _mat2.is_null(_k, _j):
                        _elem += _mat1.get_elem(_i, _k) * _mat2.get_elem(_k, _j)
                return _elem

            _mul = Sparse()
            _mul.m = self.m
            _mul.n = other.n
            for i in range(_mul.m):
                for j in range(_mul.n):
                    # calculating each element of production matrix
                    if _get_factor(self, other, i, j):
                        _mul.get_elements()[(i, j)] = _get_factor(self, other, i, j)
        else:
            raise Exception('Incorrect size of matrix')
        return _mul

    def local_min(self):
        """
        Returns minimal element of sparse matrix.
        """
        return min(self._elements.values())

    def local_max(self):
        """
        Returns maximal element of sparse matrix.
        """
        return max(self._elements.values())

    def is_diagonal(self):
        """
        Checks if matrix is diagonal.
        """
        _flag = True
        for key in self._elements:
            if key[0] != key[1] and self._elements[key] != 0:
                _flag = False
                break
        return _flag

    def is_triangular_down(self):
        _flag = True
        for key, value in self._elements.items():
            if key[0] < key[1] and value != 0:
                _flag = False
        return _flag


if __name__ == "__main__":

    mat1 = Sparse([[0, 0, 1], [0, 0, 0], [0, 2, 0]])
    mat2 = Sparse([[0, 0, 0], [0, 1, 0], [3, 0, 0]])

    # print(mat1 + mat2)
    # print(mat1 * mat2)
    # print(mat2 * mat1)
    # print(mat1.local_max())
    # print(mat1.local_min())
    # print(mat1.is_diagonal())
    # print(mat2.is_diagonal())
    # print(mat1.is_triangular_down())
    # print(mat2.is_triangular_down())
