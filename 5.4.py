def create_matrix():
    matrix = []
    for i in range(3):
        row = []
        for j in range(3):
            element = int(input(f"Enter element at position ({i+1},{j+1}): "))
            row.append(element)
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    print("Matrix:")
    for row in matrix:
        print(row)

def extract_elements(matrix):
    print("\nExtracting individual elements of the matrix:")
    for i in range(3):
        for j in range(3):
            print(f"Element at position ({i+1},{j+1}):", matrix[i][j])

def main():
    # Create a 3x3 matrix
    matrix = create_matrix()

    # Print the matrix
    print_matrix(matrix)

    # Extract individual elements of the matrix
    extract_elements(matrix)

if _name_ == "_main_":
    main()
