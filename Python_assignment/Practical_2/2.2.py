string = "Hello, World!"

length = len(string)
print("Length of the string:", length)

lowercase_string = string.lower()
print("Lowercase:", lowercase_string)

uppercase_string = string.upper()
print("Uppercase:", uppercase_string)

count_occurrences = string.count('l')
print("Occurrences of 'l':", count_occurrences)

starts_with_hello = string.startswith("Hello")
print("Starts with 'Hello':", starts_with_hello)

ends_with_world = string.endswith("World!")
print("Ends with 'World!':", ends_with_world)

index_of_comma = string.find(',')
print("Index of ',':", index_of_comma)

replaced_string = string.replace("World", "Universe")
print("Replaced string:", replaced_string)