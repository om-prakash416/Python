
thistuple= ("apple","banana","cherry")
print(thistuple)

print("***access tuple item**")
print(thistuple[1])
print("***negative index**")
print(thistuple[-1])

print("***change tuple item**")
x =("apple","banana","cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)