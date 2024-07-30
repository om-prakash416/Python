# swap the ex -or operator using third variable

# Get user input for the two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Print the numbers before swap
print(f"Numbers before swap:\n first number = {num1} \n second number = {num2}")

# Swap the numbers using XOR
num1 = num1 ^ num2
num2 = num1 ^ num2
num1 = num1 ^ num2

# Print the numbers after swap
print(f"Numbers after swap:\n first number = {num1} \n second number = {num2}")
