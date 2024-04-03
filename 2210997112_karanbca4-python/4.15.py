 
def create_and_sort_list(size):
 
    numbers = []
    print("Enter", size, "numbers:")
    for _ in range(size):
        number = int(input())
        numbers.append(number)

     
    print("\nList before sorting:", numbers)

    
    numbers.sort()

 
    print("List after sorting:", numbers)

 
def main():
    
    size = int(input("Enter the size of the list: "))

     
    if size <= 0:
        print("Please enter a positive size.")
    else:
         create_and_sort_list(size)

 
 
main()
