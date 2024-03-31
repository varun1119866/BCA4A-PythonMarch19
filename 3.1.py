print("name diksha roll no 2210997073")
def is_divisible(m, n):
    if m % n == 0:
        return True
    else:
        return False
m = int(input("Enter the first number: "))
n = int(input("Enter the second number: "))
result = is_divisible(m, n)
if result:
    print(f"{m} is divisible by {n}")
else:
    print(f"{m} is not divisible by {n}")
