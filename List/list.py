thislist = list(("apple","banana","cherry"))
print(thislist)
print(thislist[1])
print(thislist[-1])

print("*************")

thislist2 =["apple","banana","cherry","orange","kiwi","melon","mango"]
print(thislist2[2:5])
print(thislist2[:4])
print(thislist2[:5])
thislist2 = "blackberry"
print(thislist2)

thislist22 =["apple","banana","cherry","orange","kiwi","melon","mango"]
thislist22[1:3]=["blackcurrent","watermelon"]
print(thislist22)

thislist3 = ["apple","banana","cherry"]
thislist3.insert(2,"watermelon")
print(thislist3)

thislist4 = ["apple","banana","cherry"]
thislist4.append("orange")
print(thislist4)

thislist5 = ["apple","banana","cherry"]
tropical = ["mango","pineapple","papaya"]
thislist5.extend(tropical)
print(thislist5)

#remove specified item
thislist6 = ["apple","banana","cherry"]
thislist6.remove("banana")
print(thislist6)

#remove specified index
thislist7 = ["apple","banana","cherry"]
thislist7.pop(1)
print(thislist7)

thislist8 = ["apple","banana","cherry"]
thislist8.pop()
print(thislist7)

#del
thislist9 = ["apple","banana","cherry"]
del thislist9[0]
print(thislist9)

thislist23 = ["apple","banana","cherry"]
del thislist23
print(thislist23)

#clear the list
thislist11 = ["apple","banana","cherry"]
thislist11.clear()
print(thislist11)

#sortlist alphanumerically

thislist12=["apple","banana","cherry","orange","kiwi","melon","mango"]
thislist12.sort()
print(thislist12)

thislist13 =["apple","banana","cherry","orange","kiwi","melon","mango"]
thislist13.sort(reverse =True)
print(thislist13)

#reverese order

thislist14 =["apple","banana","cherry","orange","kiwi","melon","mango"]
thislist14.reverse()
print(thislist14)

# sort descending
thislist15 =["apple","banana","cherry","orange","kiwi","melon","mango"]
thislist15.sort(reverse =True)
print(thislist15)

#copy
thislist16 =["apple","Banana","Cherry"]
mylist = thislist16.copy()
print(mylist)

#join list
list1 = ["a","b","c"]
list2 = [1,2,3]
list3 = list1 + list2
print(list3)
 
