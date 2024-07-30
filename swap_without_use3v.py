# swap the  without using third variable

num1=int(input("Enter first number: "))
num2 = int(input("Enter 2nd number: "))

print(f"Number before swap :\n first number = {num1} \n second number = {num2} ")

num1 = num2+num1
num2 = num1-num2
num1 = num1- num2


print(f"Number after Swap:\n first number = {num1} \n second number = {num2}")