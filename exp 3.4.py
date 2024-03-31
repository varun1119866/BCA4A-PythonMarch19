def calculate_salary(bs):
    if bs >= 20000:
        da = 0.3 * bs
        hra = 0.2 * bs
    else:
        da = 0.2 * bs
        hra = 0.1 * bs
    
    print(f"Basic Salary: {bs}")
    print(f"DA: {da}")
    print(f"HRA: {hra}")

def main():
    bs = float(input("Enter Basic Salary: "))
    calculate_salary(bs)

if __name__ == "__main__":
    main()
