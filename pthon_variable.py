# many values to multiple variables

# python allows you to assign values to multiple variable in one line:

x,y,z = "oranges","Banana","Cherry"
print(x)
print(y)
print(z)

print("*********************")
# one value to multiple variables
x=y=z ="Orange"
print(x)
print(y)
print(z)

print("**************************")

# unpack a collection

fruits = ["apple","banana","cherry"]
x,y,z = fruits
print(x)
print(y)
print(z)

print("*********************")

x = "awesome"
def myfunc():
    print("Python is "+x)
myfunc()
