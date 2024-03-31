def check_divisibility(num, divisor):
    if num % divisor == 0:
        return True
    else:
        return False

def main():
    num = int(input("Enter the number: "))
    divisor = int(input("Enter the divisor: "))

    if check_divisibility(num, divisor):
        print(f"{num} is divisible by {divisor}.")
    else:
        print(f"{num} is not divisible by {divisor}.")

if _name_ == "_main_":
    main()
