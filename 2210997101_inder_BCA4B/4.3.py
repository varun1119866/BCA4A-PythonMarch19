 
print("Demonstrating the 'break' statement:")
count = 0
while True: 
    print(count, end=" ")
    count += 1
    if count >= 5:
        break   
print("\nOut of the loop after encountering 'break'")

print("\nDemonstrating the 'continue' statement:")
 
print("Skipping odd numbers:")
for num in range(10):
    if num % 2 != 0:   
        continue  
    print(num, end=" ")
print("\nOut of the loop after encountering 'continue'")
