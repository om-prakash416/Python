# swap the number using third variable4

num1=int(input("Enter first number: "))
num2 = int(input("Enter 2nd number: "))

print(f"Number before swap :\n first number = {num1} \n second number = {num2} ")

temp = num1
num1 = num2
num2 = temp

print(f"Number after Swap:\n first number = {num1} \n second number = {num2}")