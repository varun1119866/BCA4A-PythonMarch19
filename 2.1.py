# Define a string
my_string = "Hello, World!"

# Basic slicing - extracting a substring
substring1 = my_string[7:]  # Get characters from index 7 to the end
substring2 = my_string[:5]  # Get characters from the beginning to index 5 (exclusive)
substring3 = my_string[2:5]  # Get characters from index 2 to index 5 (exclusive)
substring4 = my_string[::2]  # Get every second character
substring5 = my_string[::-1]  # Reverse the string

# Display results
print("Original String:", my_string)
print("Substring from index 7 to the end:", substring1)
print("Substring from the beginning to index 5:", substring2)
print("Substring from index 2 to index 5:", substring3)
print("Every second character:", substring4)
print("Reversed string:", substring5)
