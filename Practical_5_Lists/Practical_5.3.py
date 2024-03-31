#WAP to demonstrate the working of methods used with lists

print("Name : Simranjeet Kaur\nRoll number : 2210997238\n")

names = ['Aman', 'Raman', 'Sham', 'Raj', 'Ramesh', 'Tarun', 'Garima']

print("Original list:", names)

# Append method
names.append('Sonia')
print("\nAfter appending 'Sonia':", names)

# Insert method 
names.insert(2, 'Ram')
print("After inserting 'Ram' at index 2:", names)

# Remove method 
names.remove('Sham')
print("After removing 'Sham':", names)

# Pop method 
popped_name = names.pop(4)
print("Popped name at index 4:", popped_name)
print("After popping name at index 4:", names)

# Extend method
names.extend(['Anita', 'Vikram'])
print("After extending with ['Anita', 'Vikram']:", names)

# Index method 
index = names.index('Raj')
print("Index of 'Raj':", index)

# Count method 
count = names.count('Aman')
print("Number of occurrences of 'Aman':", count)

# Sort method 
names.sort()
print("After sorting in alphabetical order:", names)

# Reverse method 
names.reverse()
print("After reversing:", names)

# Clear method -
names.clear()
print("After clearing the list:", names)
