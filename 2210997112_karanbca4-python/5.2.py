my_list = ['q', 'w', 'e', 'r', 't', 'y']

for index, item in enumerate(my_list):
    print(f"Element '{item}' at index {index} (Positive) and {index - len(my_list)} (Negative)")
