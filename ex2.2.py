# Program to demonstrate built-in functions of strings

string = "Hello, World!"

print("Length of string:", len(string))

print("Uppercase string:", string.upper())

print("Lowercase string:", string.lower())

substring = "l"
print("Occurrences of 'l' in string:", string.count(substring))

substring = "World"
print("Index of 'World' in string:", string.find(substring))

old_substring = "World"
new_substring = "Universe"
new_string = string.replace(old_substring, new_substring)
print("String after replacement:", new_string)

split_string = string.split(", ")
print("Split string:", split_string)
