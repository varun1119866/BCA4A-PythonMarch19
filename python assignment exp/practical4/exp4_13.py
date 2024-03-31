n = int(input("Enter a positive integer: "))
total = 0

if n < 0:
    print("Enter a positive integer")
else:
    for i in range(1, n + 1):
        total += i

print("Sum of first", n, "natural numbers:", total)
