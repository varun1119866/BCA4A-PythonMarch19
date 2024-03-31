def check_number_sign(number):
  
  if number > 0:
    return "Positive"
  elif number < 0:
    return "Negative"
  else:
    return "Zero"

number = float(input("Enter a number: "))

sign = check_number_sign(number)
print(f"The number {number} is {sign}.")
print("Garima Jain\n22109971080\nBCA4 B-1")