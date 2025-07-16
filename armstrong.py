num=int(input('enter number to check armstrong or not: '))

arms= num

length= len(str(num))

sum1=0

while num !=0:
    rem= num%10
    sum1=sum1+(rem**length)
    num=num//10
    
if arms ==sum1:
    print("the given number is",arms, "is armstrong number")
else:
    print("the given number",arms,"is not an armstrong number")