print("NAME : RAGHAV \n ROLL NO : 2210997182")
# Demonstration of break statement
print("Demonstration of break statement:")
for i in range(1, 11):
    if i == 6:
        break  # Exit the loop when i equals 6
    print(i, end=" ")
print("\n")

# Demonstration of continue statement
print("Demonstration of continue statement:")
for i in range(1, 11):
    if i == 3 or i == 7:
        continue  # Skip printing i when it equals 3 or 7
    print(i, end=" ")
