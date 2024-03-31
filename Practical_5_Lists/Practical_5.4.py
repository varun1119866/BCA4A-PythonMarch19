#WAP to create a 3*3 Matrix and how to extract individual elements of the matrix

print("Name : Simranjeet Kaur\nRoll number : 2210997238\n")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:")
for row in matrix:
    print(row)

# Extracting elements
print("\nExtracting all elements:")
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print("Element at [", i, ",", j, "]:", matrix[i][j])
