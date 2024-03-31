def main():
    # Creating a list
    my_list = ['apple', 'banana', 'cherry', 'apple']

    # Append: Add an element to the end of the list
    my_list.append('orange')
    print("List after appending 'orange':", my_list)

    # Extend: Add elements from another list to the end of the list
    another_list = ['grape', 'mango']
    my_list.extend(another_list)
    print("List after extending with another list:", my_list)

    # Insert: Insert an element at a specific position
    my_list.insert(2, 'pear')
    print("List after inserting 'pear' at index 2:", my_list)

    # Remove: Remove the first occurrence of a value from the list
    my_list.remove('apple')
    print("List after removing the first occurrence of 'apple':", my_list)

    # Pop: Remove and return the element at a specific index
    popped_element = my_list.pop(3)
    print("Popped element:", popped_element)
    print("List after popping element at index 3:", my_list)

    # Index: Return the index of the first occurrence of a value
    index_of_banana = my_list.index('banana')
    print("Index of 'banana':", index_of_banana)

    # Count: Count the number of occurrences of a value
    count_of_apple = my_list.count('apple')
    print("Count of 'apple':", count_of_apple)

    # Reverse: Reverse the elements of the list in place
    my_list.reverse()
    print("List after reversing:", my_list)

    # Sort: Sort the elements of the list in place
    my_list.sort()
    print("List after sorting:", my_list)

    # Clear: Remove all elements from the list
    my_list.clear()
    print("List after clearing:", my_list)

if _name_ == "_main_":
    main()
