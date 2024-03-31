def check_number(num):
    if num > 0:
        print("Positive number")
    elif num < 0:
        print("Negative number")
    else:
        print("Zero")

def main():
    num = float(input("Enter a number: "))
    check_number(num)

if __name__ == "__main__":
    main()
