my_string = "Hello, World!"

string_length = len(my_string)
print("Length of the string:", string_length)

uppercase_string = my_string.upper()
print("Uppercase:", uppercase_string)

lowercase_string = my_string.lower()
print("Lowercase:", lowercase_string)

is_present = "World" in my_string
print("Does the string contain 'World'?", is_present)

does_start = my_string.startswith("Hello")
print("Does the string start with 'Hello'?", does_start)

does_end = my_string.endswith("!")
print("Does the string end with '!'?", does_end)

trimmed_string = my_string.strip()
print("String after removing leading/trailing whitespaces:", trimmed_string)

replaced_string = my_string.replace("Hello", "Hi")
print("String with 'Hello' replaced with 'Hi':", replaced_string)

string_list = my_string.split(",")
print("String split into a list:", string_list)

print("Garima Jain\n22109971080\nBCA4 B-1")