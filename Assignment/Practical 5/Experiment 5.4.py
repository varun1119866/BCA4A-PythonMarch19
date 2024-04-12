#WAP to create a 3*3 Matrix and how to extract individual elements of the matrix
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j],end=" ")
    print()