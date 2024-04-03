 
def cube(n):
    return n ** 3

 
def main():
    print("Cube of the first 10 even numbers:")
    count = 0
    for num in range(2, 21, 2):
        print("Cube of", num, ":", cube(num))
        count += 1
        if count == 10:  
            break

 
main()
