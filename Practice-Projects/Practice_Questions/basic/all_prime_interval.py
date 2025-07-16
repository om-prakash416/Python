
def disp_prime(num1,num2):
    prime_list = []
    for i in range(num1,num2):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2,int(i/2)+1):
                if  i % j == 0:
                    break
            else:
                prime_list.append(i)
    return prime_list

starting_Num = int(input("Enter the starting range: "))
ending_num = int(input("enter the ending range: "))

lst = disp_prime(starting_Num,ending_num)
if len(lst) == 0:
    print("There are no prime numbers in this range")

else:
    print("the prime numbers in the given range are: ",lst)