#5.1

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




#5.2
elements = ['q', 'w', 'e', 'r', 't', 'y']

for i, element in enumerate(elements):
    print("Element:", element)
    print("Positive Index:", i)
    print("Negative Index:", i - len(elements))
    print() 


#5.3
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




#5.4
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:")
for row in matrix:
    print(row)
# Extracting elements
print("\nExtracting all elements:")
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print("Element at [", i, ",", j, "]:", matrix[i][j])


#5.5
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]

print("Original list:", my_list)

# len()
print("\nLength of the list:", len(my_list))

# min()
print("Minimum value in the list:", min(my_list))

# max()
print("Maximum value in the list:", max(my_list))

# sum()
print("Sum of all elements in the list:", sum(my_list))

# sorted()
sorted_list = sorted(my_list)
print("\nSorted list:", sorted_list)

# reversed()
reversed_list = list(reversed(my_list))
print("Reversed list:", reversed_list)

# count() 
count = my_list.count(5)
print("\nNumber of occurrences of 5 in the list:", count)

# index() 
index_9 = my_list.index(9)
print("Index of first occurrence of 9 in the list:", index_9)

my_list.append(7)
print("\nAfter appending 7:", my_list)

# insert() 
my_list.insert(3, 3.5)
print("After inserting 3.5 at index 3:", my_list)

# remove() 
my_list.remove(9)
print("After removing the first occurrence of 9:", my_list)

# pop()
popped_element = my_list.pop(4)
print("Popped element at index 4:", popped_element)
print("After popping element at index 4:", my_list)

# clear() 
my_list.clear()
print("\nAfter clearing the list:", my_list)


#5.6
#WAP to calculate the mean, variance and std. deviation of given list of numbers
import statistics

numbers = [4, 5, 8, 9, 11, 15, 18]

# mean
mean = statistics.mean(numbers)

# variance
variance = statistics.variance(numbers)

# standard deviation
std_deviation = statistics.stdev(numbers)

print("Given list of numbers:", numbers)
print("Mean:", mean)
print("Variance:", variance)
print("Standard deviation:", std_deviation)