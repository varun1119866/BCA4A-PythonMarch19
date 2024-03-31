print("Shikha - 2210997218")
print(" ")

numbers = [3, 1, 4, 1, 5, 9, 2, 6]

print(" ")
numbers.append(8)
print("After appending 8:", numbers)

print(" ")
numbers.insert(3, 7)
print("After inserting 7 at index 3:", numbers)

print(" ")
numbers.remove(1)
print("After removing 1:", numbers)

print(" ")
popped_element = numbers.pop(4)
print("Popped element:", popped_element)

print(" ")
print("List after popping:", numbers)

print(" ")
count_2 = numbers.count(2)
print("Number of 2s in the list:", count_2)

print(" ")
numbers.reverse()
print("Reversed list:", numbers)

print(" ")
numbers.sort()
print("Sorted list:", numbers)
