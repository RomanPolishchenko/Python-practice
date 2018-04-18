import copy


def input_matrix(filename):
    f = open(filename, 'r')
    _matrix = []
    for lane in f:
        _matrix.append(list(map(float, lane.split())))
    f.close()
    return _matrix


def print_matrix(matrix):
    if type(matrix) is list:
        for row in matrix:
            print(*row)
    else:
        print(matrix)


def multi(matrix_1, matrix_2):
    _matrix = [[0 for j in range(len(matrix_2[0]))] for i in range(len(matrix_1))]
    x = len(matrix_1[0])
    y = len(matrix_2)
    if x == y:
        m = len(_matrix)
        n = len(_matrix[0])
        for i in range(m):
            for j in range(n):
                _matrix[i][j] = 0
                for k in range(x):
                    _matrix[i][j] += matrix_1[i][k] * matrix_2[k][j]
    else:
        _matrix = 'Inconsistent row/column dimensions.'
    # _matrix = [[sum(map(lambda x: x[0] * x[1], zip(matrix_1[i], [c[j] for c in matrix_2]))) \
    # for j in range(len(matrix_2[0]))] for i in
    #      range(len(matrix_1))]
    return _matrix


def swap_rows(matrix, row1, row2):
    matrix[row1], matrix[row2] = matrix[row2], matrix[row1]


def swap_columns(matrix, column1, column2):
    for row in matrix:
        row[column1], row[column2] = row[column2], row[column1]


def get_row(matrix, row_num):
    return matrix[row_num]


def multi_by_num(matrix, num):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] *= num


def to_triangle_type(matrix):
    for k in range(len(matrix)):
        for i in range(k + 1, len(matrix[0])):
            r = 1
            while matrix[k][k] == 0 and k + r < len(matrix):
                swap_rows(matrix, k, k + r)
                r += 1
            if matrix[k][k] == 0:
                return 0
            coe = matrix[i][k]/matrix[k][k]
            for j in range(len(matrix[0])):
                matrix[i][j] -= matrix[k][j]*coe
    return 1


def minor(matrix, m, n):
    _minor = copy.deepcopy(matrix)
    del _minor[m]
    for row in _minor:
        del row[n]
    return _minor


def determinant(matrix):
    _det = 0
    if len(matrix) != len(matrix[0]):
        _det = 'Wrong type for input argument #1: Square matrix expected.'
    else:
        n = len(matrix)
        if n == 1:
            _det = matrix[0][0]
        else:
            for j in range(n):
                _det += (-1)**(2+j) * matrix[0][j] * determinant(minor(matrix, 0, j))
    return _det

a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

