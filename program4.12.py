print("Shikha - 2210997218")
print(" ")

# Initialize variables
even_numbers = []
count = 1

# Find first 10 even numbers and their cubes
while len(even_numbers) < 10:
    if count % 2 == 0:
        even_numbers.append(count ** 3)
    count += 1

print("Cube of first 10 even numbers:", even_numbers)
