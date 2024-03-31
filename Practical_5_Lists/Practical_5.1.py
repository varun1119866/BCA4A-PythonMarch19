#WAP to show the creation and working of lists

print("Name : Simranjeet Kaur\nRoll number : 2210997238\n")

#creating list
names = ['Aman', 'Raman', 'Sham', 'Raj', 'Ramesh', 'Tarun', 'Garima']

print("Original list of names:", names)

# Accessing elements 
print("\nAccessing elements of the list:")
print("First name:", names[0])
print("Second name:", names[1])
print("Last name:", names[-1])

# Modifying elements 
names[1] = 'Ram' 
print("\nModified list of names after replacing 'Raman' with 'Ram':", names)

# Adding elements
names.append('Sonia')
print("\nList of names after adding 'Sonia':", names)

# Removing elements 
removed_name = names.pop(2)
print("\nList of names after removing", removed_name + ":", names)

# Slicing list
print("\nSlicing the list to get a sublist:")
sublist = names[1:4]
print("Sublist of names:", sublist)

# Iterating
print("\nIterating over elements of the list:")
for name in names:
    print(name)

# Checking if an element exists in the list
print("\nChecking if an element exists in the list:")
if 'Aman' in names:
    print("Yes, 'Aman' exists in the list")
else:
    print("No, 'Aman' does not exist in the list")
