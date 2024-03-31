print("Shikha - 2210997218")
print(" ")

letters = ['q', 'w', 'e', 'r', 't', 'y']

# Print elements in 3 separate lines with both positive and negative indexes
for i in range(len(letters)):
    print(f"Element '{letters[i]}' at index {i} (positive) and index {-len(letters) + i} (negative)")
