num1 = int(input('Enter the first variable: '))
num2 = int(input('Enter the second variable: '))

print("the value of num1 and num2 before the swapping: {0} , {1} ".format(num1, num2))

# temp = num1
# num1 = num2
# num2 = temp

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2



print('the value of num1 after swapping:{0} , {1} '.format(num1, num2))


