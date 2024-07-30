m = [[11,2],[3,341,5],[53]]

max_value = float("-inf")

for sublist in m:
    for num in sublist:
        if num > max_value:
            max_value = num 
            
            
print("Maximum value: ",max_value)

y=min(5,10,25)
print(y)
x=max(5,10,25)
print(x)