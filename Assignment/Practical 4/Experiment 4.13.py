# compute sum of first n natural numbers
print("Name: Dhriti Gandhi\nRoll No: 2210997070")

n = int(input("Enter a number: "))
sum = 0

for i in range(1, n+1):
    sum = sum + i
print(f"Sum of first {n} natural numbers: {sum}")