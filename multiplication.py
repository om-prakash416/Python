def print_multiplication_table(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n * i}")
        
number  = int(input("Enter a number: "))

print_multiplication_table(number)