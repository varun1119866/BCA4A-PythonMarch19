#WAP to demonstrate built in functions of Strings

print("Name : Simranjeet Kaur\nRoll number : 2210997238\n")

#length
string = "Simranjeet Kaur"
print("Length of the string:", len(string))
#lowercase
print("Lowercase:", string.lower())
#uppercase
print("Uppercase:", string.upper())
#count
substring = "a"
print("Occurrences of 'a':", string.count(substring))
#find
substring = "Kaur"
print("Index of 'Kaur':", string.find(substring))
#startswith
substring = "Simranjeet"
print("Starts with 'Simranjeet':", string.startswith(substring))
#endswith
substring = "Kaur"
print("Ends with 'Kaur':", string.endswith(substring))
#replace
old_substring = "Kaur"
new_substring = "Hello"
new_string = string.replace(old_substring, new_substring)
print("After replacement:", new_string)
#split
words = string.split(",")
print("Splitting the string:", words)
#capitalize
print("capitalize():", string.capitalize())
#isalpha
print("isalpha():", string.isalpha())
#isnumeric
print("isnumeric",string.isnumeric())
#isdigit
print("isdigit():", string.isdigit())
#islower
print("islower():", string.islower())
#isupper
print("isupper():", string.isupper())
#isspace
print("isspace():", string.isspace())
#format
print("format():", "Hello, {}!".format("world"))
#rfind
print("rfind('e'):", string.rfind("e"))
#rindex
print("rindex('m'):", string.rindex("m"))