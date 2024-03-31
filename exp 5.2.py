my_list = ['a', 'n', 'j', 'a', 'l', 'i']

for index, value in enumerate(my_list):
    print(f"Index {index} (Positive): {value}")
    print(f"Index {-len(my_list) + index} (Negative): {value}")
