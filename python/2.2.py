print("NAME : RAHUL SINGH \n ROLL NO : 2210997186")
# Define a sample string
sample_string = "Hello, World!"

# Length of the string
print("Length of the string:", len(sample_string))

# Convert to lowercase and uppercase
print("Lowercase:", sample_string.lower())
print("Uppercase:", sample_string.upper())

# Count occurrences of a substring
print("Occurrences of 'l':", sample_string.count('l'))

# Find the index of a substring
print("Index of 'World':", sample_string.find('World'))

# Replace a substring
print("Replace 'World' with 'Universe':", sample_string.replace('World', 'Universe'))

# Check if the string starts/ends with a particular substring
print("Starts with 'Hello':", sample_string.startswith('Hello'))
print("Ends with 'World!':", sample_string.endswith('World!'))

# Split the string into a list based on a delimiter
print("Split by comma:", sample_string.split(','))

# Join elements of a list into a single string
words = ['Hello', 'World', 'Python']
print("Joined string:", ' '.join(words))

# Check if the string contains only alphanumeric characters
print("Is alphanumeric:", sample_string.isalnum())

# Check if the string contains only alphabetical characters
print("Is alphabetic:", sample_string.isalpha())

# Check if the string contains only digits
numeric_string = "12345"
print("Is numeric:", numeric_string.isdigit())
