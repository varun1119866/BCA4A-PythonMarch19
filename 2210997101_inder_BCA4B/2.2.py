def main():
    string = input("Enter a string: ")

    print("Length of the string:", len(string))
    print("Uppercase string:", string.upper())
    print("Lowercase string:", string.lower())
    print("Capitalized string:", string.capitalize())
    print("Number of 'l's in the string:", string.count('l'))
    print("Index of 'o' in the string:", string.find('o'))
    
    replace_string = input("Enter a string to replace (if any): ")
    replace_with = input("Enter a string to replace with: ")
    replaced_string = string.replace(replace_string, replace_with)
    print("Replacing '{}' with '{}':".format(replace_string, replace_with), replaced_string)
    
    print("Splitting the string by comma:", string.split(','))
    words = input("Enter words separated by spaces: ").split()
    print("Joining the words with space separator:", ' '.join(words))

if __name__ == "__main__":
    main()
