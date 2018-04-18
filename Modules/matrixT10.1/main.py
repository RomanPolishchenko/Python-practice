from matrix_module import *

if __name__ == '__main__':
    matrix1 = input_matrix('matrix1.txt')
    matrix2 = input_matrix('matrix2.txt')
    # print_matrix(multi(matrix1, matrix2))
    # print_matrix(multi(matrix2, matrix1))
    # swap_rows(matrix1, 0, 1)
    # swap_columns(matrix1, 0, 1)
    # multi_by_num(matrix1, 2)
    # to_triangle_type(matrix1)
    # print_matrix(matrix1)
    # mi = minor(matrix1, 0, 0)

    print_matrix(determinant(matrix1))
