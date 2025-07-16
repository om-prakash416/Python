import math

def check_fact(num):
    return (math.factorial(num))

num = int(input("enter then number to find factorial: "))
fact = check_fact(num)
print("Factorial of", num, "is", fact)