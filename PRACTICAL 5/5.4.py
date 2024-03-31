# WAP to create a 3*3 Matrix and how to extract individual elements of the matrix

matrix = [[11, 12, 23],
          [45, 65, 36],
          [17, 38, 99]]

print("Individual elements of the matrix:")
for i in range(3):
    for j in range(3):
        print("Element at ({}, {}): {}".format(i, j, matrix[i][j]))
