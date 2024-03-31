# WAP to show the working of break and continue statement

print("Name : Simranjeet Kaur\nRoll number : 2210997238\n")

print("Using break")
for i in range(1, 11):
    if i == 5:
        print("Encountered 5, breaking loop")
        break
    print("Current value of i:", i)
print("Loop ended")

print("\nUsing continue")
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print("Current value of i:", i)
print("Loop ended")
