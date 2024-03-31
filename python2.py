#pracical 2
#2.1
# Slicing Operations in Strings
string_example = "Hello, World!"

# Slicing to get a substring
substring = string_example[7:]  # Slicing from index 7 till the end
print("Substring:", substring)

# Slicing with a step
substring_with_step = string_example[::2]  # Slicing with a step of 2
print("Substring with step:", substring_with_step)

# Slicing with negative indices
substring_negative_indices = string_example[-6:-1]  # Slicing from the 6th last character to the 2nd last character
print("Substring with negative indices:", substring_negative_indices)
#2.2
# Built-in functions of Strings
# 1. len() - to get the length of a string
length_of_string = len(string_example)
print("Length of the string:", length_of_string)

# 2. upper() - to convert the string to uppercase
upper_case_string = string_example.upper()
print("Uppercase string:", upper_case_string)

# 3. lower() - to convert the string to lowercase
lower_case_string = string_example.lower()
print("Lowercase string:", lower_case_string)

# 4. split() - to split the string into a list of substrings based on a delimiter
split_string = string_example.split(",")  # Splitting based on comma
print("Split string:", split_string)

# 5. strip() - to remove leading and trailing whitespaces from a string
string_with_spaces = "   Hello, World!   "
stripped_string = string_with_spaces.strip()
print("Stripped string:", stripped_string)

# 6. replace() - to replace occurrences of a substring within a string
replaced_string = string_example.replace("Hello", "Hi")
print("Replaced string:", replaced_string)

# 7. find() - to find the index of the first occurrence of a substring within a string
index = string_example.find("World")
print("Index of 'World':", index)
