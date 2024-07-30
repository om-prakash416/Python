class A:
    def myfun(self):
        print("In class A")
class B(A):
        def myfun(self):
            print("in class B")
class C(A):
     def myfun(self):
          print("in class C")
#classes ordering

class D(B,C):
     pass
r =D()
r.myfun()


print("******************")

class Person(object):
     #Constructor
    def __init__(self,name):
          self.name = name
    # to get name
    def getName(self):
     return self.name
    # to check if this person is an employee
    def isEmployee(self):
         return False

#inheritated or subclaa (note person in bracket)
class Employee(Person):
    #  here we return true 
    def isEmployee(self):
     return True

# driver Code
emp = Person("om1") #an object of person
print(emp.getName(),emp.isEmployee())

emp = Employee("om2") #an object of employee
print(emp.getName(),emp.isEmployee())




    