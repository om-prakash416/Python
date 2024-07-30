# l1= [1,2,3]
# l2=['a','b','c']

# for i in l1:
#     j=0
#     while(j<len(l2)):
#         print(i,l2[j])
#         j=j+1
        
        
# l1 = [2,4,5,67,21,45,10,11]
# oddlist=[]
# for i  in l1:
#     if(i%2!=0):
#         oddlist.append(i)
# oddlist

l=[4,53,3,6,9,8,14,10,11,13]
oddlist=[]
for i in l[:]:
    if(i%2!=0):
        oddlist.append(i)
print("Final list: ",oddlist)
