def main():
    even_numbers = [2 * i for i in range(1, 11)]  # Generating first 10 even numbers
    cube_of_even_numbers = [num ** 3 for num in even_numbers]  # Calculating cube of even numbers

    print("Cube of the first 10 even numbers:")
    for i in range(10):
        print(f"Cube of {even_numbers[i]}:", cube_of_even_numbers[i])

if _name_ == "_main_":
    main()
