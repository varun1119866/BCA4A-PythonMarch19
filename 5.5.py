def main():
    # Create a list
    my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

    # Length of the list
    print("Length of the list:", len(my_list))

    # Maximum element in the list
    print("Maximum element in the list:", max(my_list))

    # Minimum element in the list
    print("Minimum element in the list:", min(my_list))

    # Sum of all elements in the list
    print("Sum of all elements in the list:", sum(my_list))

    # Sort the list in ascending order
    sorted_list = sorted(my_list)
    print("Sorted list in ascending order:", sorted_list)

    # Reverse the list in place
    my_list.reverse()
    print("List after reversing in place:", my_list)

    # Count occurrences of an element in the list
    count_of_5 = my_list.count(5)
    print("Count of occurrences of 5 in the list:", count_of_5)

    # Append an element to the end of the list
    my_list.append(8)
    print("List after appending 8:", my_list)

    # Insert an element at a specific position
    my_list.insert(2, 7)
    print("List after inserting 7 at index 2:", my_list)

    # Remove the first occurrence of an element from the list
    my_list.remove(3)
    print("List after removing the first occurrence of 3:", my_list)

    # Pop the element at a specific position
    popped_element = my_list.pop(4)
    print("Popped element:", popped_element)
    print("List after popping element at index 4:", my_list)

if _name_ == "_main_":
    main()
