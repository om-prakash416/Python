def check_number_properties(n):
    if n%4 == 0:
        print(f"{n} is divisible by 4.")
    else:
        print(f"{n} is not divisible by 4.")
    
    if n%2 == 0:
        print(f"{n} is an even number.")
    else:
        print(f"{n} is an odd number.")
        
number = int(input("Enter a number: "))
 
check_number_properties(number)