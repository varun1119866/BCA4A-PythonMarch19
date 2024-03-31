def main():
    # Example of break statement
    print("Example of break statement:")
    for i in range(1, 11):
        if i == 6:
            break  # Exit the loop when i equals 6
        print(i, end=' ')
    print("\nLoop ended due to break statement\n")

    # Example of continue statement
    print("Example of continue statement:")
    for i in range(1, 11):
        if i % 2 == 0:
            continue  # Skip even numbers
        print(i, end=' ')
    print("\nLoop ended normally after using continue statement")

if _name_ == "_main_":
    main()
