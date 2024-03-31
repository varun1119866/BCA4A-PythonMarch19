def calculate_commission(sales_amount):
    if sales_amount >= 15000:
        commission = 0.20 * sales_amount
    elif sales_amount >= 1000:
        commission = 0.15 * sales_amount
    else:
        commission = 0.10 * sales_amount
    
    print(f"Sales Amount: {sales_amount}")
    print(f"Commission: {commission}")

def main():
    sales_amount = float(input("Enter Sales Amount: "))
    calculate_commission(sales_amount)

if __name__ == "__main__":
    main()
