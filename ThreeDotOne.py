def is_divisible(num1, num2):
  
  return num1 % num2 == 0

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

if is_divisible(number1, number2):
  print(f"{number1} is divisible by {number2}.")
else:
  print(f"{number1} is not divisible by {number2}.")
print("Karan Arora\n2210997111\nBCA4 B-1")
