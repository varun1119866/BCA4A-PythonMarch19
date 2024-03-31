def main():
    string = input("Enter String:")
    print("Original string:", string)
    print("First five characters:", string[:5])
    print("Characters from index 7 to 11:", string[7:12])
    print("Last five characters:", string[-5:])
    print()
    print("Every second character:", string[::2])
    print("Characters in reverse:", string[::-1])
    print()
    print("Every second character (alternative method):", string[1::2])
    print()
    print("String in reverse (alternative method):", string[::-1])
    print()

if __name__ == "__main__":
    main()
