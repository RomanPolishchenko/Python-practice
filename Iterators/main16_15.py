matrix = [[1, 2, 3], [4, 5, 6]]

rez = ((matrix[i][j], i, j) for i in range(len(matrix)) for j in range(len(matrix[0])))

for i in rez:
    print(i)

for i in ((matrix[i][j], i, j) for i in range(len(matrix)) for j in range(len(matrix[0]))):
    print(i)
