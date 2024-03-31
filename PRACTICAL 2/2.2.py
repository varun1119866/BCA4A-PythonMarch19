# WAP to demonstrate built-in functions of Strings

a = "My roll no is 7237"

print("Length of the string:", len(a))

uppercase_string = a.upper()
print("Uppercase string:", uppercase_string)

lowercase_string = a.lower()
print("Lowercase string:", lowercase_string)

substring_count = a.count("o")
print("Number of occurrences of 'o':", substring_count)

substring_index = a.find("roll")
print("Index of 'roll':", substring_index)

replaced_string = a.replace("My", "Your")
print("String after replacement:", replaced_string)

splitted_string = a.split(" ")
print("String after splitting by space:", splitted_string)

joined_string = "-".join(["apple", "banana", "cherry"])
print("Joined string:", joined_string)

starts_with_hello = a.startswith("Hello")
print("Starts with 'Hello':", starts_with_hello)

ends_with_world = a.endswith("world!")
print("Ends with 'world!':", ends_with_world)

print("Is there any whitespace?", a.isspace())

last_substring_index = a.rfind("o")
print("Last index of 'o':", last_substring_index)

last_substring_index = a.rindex("o")
print("Last index of 'o':", last_substring_index)
