print ("Name: Arpita Chaudhary\nRoll No: 2210997047")

numbers = [9, 3, 2, 5, 1, -9]

total = sum(numbers)
print("Sum of the list: ", total)

min_num = min(numbers)
print("Smallest number: ", min_num)


max_num = max(numbers)
print("Largest number: ", max_num)


list_length = len(numbers)
print("Length of the list: ", list_length)


sorted_numbers = sorted(numbers)
print("Sorted list: ", sorted_numbers)


numbers.reverse()
print("Reversed list: ", numbers)


numbers.sort()
print("Sort list in-place: ", numbers)


numbers.append(3)
print("Append 3: ", numbers)


numbers.insert(2, 7)
print("Insert 7 at position 2: ", numbers)


occurrences = numbers.count(5)
print("Occurrences of 5: ", occurrences)


numbers.remove(9)
print("Remove 9: ", numbers)


element = numbers.pop(1)
print("Pop element at position 1: ", element)
