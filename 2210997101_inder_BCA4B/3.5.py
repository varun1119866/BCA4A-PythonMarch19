def calculate_commission(sales_amount):
    if sales_amount >= 15000:
        commission = 0.20 * sales_amount
    elif sales_amount >= 1000:
        commission = 0.15 * sales_amount
    else:
        commission = 0.10 * sales_amount
    
    return commission

def main():
    sales_amount = float(input("Enter the sales amount: "))

    commission = calculate_commission(sales_amount)

    print("Commission:", commission)

if __name__ == "__main__":
    main()
