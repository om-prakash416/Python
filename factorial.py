# def factorial(n):
#     if n < 0:
#         return "factorial is not defined for negative number."
#     result = 1
#     for i in range(1,n+1):
#         result *=i
#     return result

# number = int(input("Enter a number: "))

# print(f"The factorial of {number} is {factorial(number)}.")

def factorial(n):
    if n<0:
       return "factorial is not defined for negative number."
    if n == 0 or n ==1:
       return 1
    else:
       return n *factorial(n-1)
   
number = int(input("Enter a number: "))
print(f"The factorial of {number} is {factorial(number)}.")