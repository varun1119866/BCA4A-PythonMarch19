#Working with Strings – basic String Operations
#WAP to demonstrate Slicing Operations in Strings

print("Name : Simranjeet Kaur\nRoll number : 2210997238\n")

string = "Hello, World!"

substring = string[7:] 
print("Substring:", substring)

part_of_string = string[2:5]  
print("Part of the string:", part_of_string)

step_slice = string[::2]  
print("Step slice:", step_slice)

reverse_slice = string[::-1] 
print("Reverse slice:", reverse_slice)

#pattern
string = "HELLO"
print("\nPattern")
for i in range(1, len(string) + 1):
    print(string[:i])
