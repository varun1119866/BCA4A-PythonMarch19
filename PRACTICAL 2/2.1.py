# WAP to demonstrate Slicing Operations in Strings

a = "Welcome to Chitkara University!"
print("Original string:", a)

substring = a[2:10]
print("Substring from index 2 to 9:", substring)

start = a[:5]
print("Substring from beginning to index 4:", start)

end = a[12:]
print("Substring from index 12 to the end:", end)

negative = a[-6:-1]
print("Substring from index -6 to -2:", negative)
