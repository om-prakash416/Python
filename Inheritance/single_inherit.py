class Person:
    def __init__(self,fname,lname):
        self.firstname =fname
        self.lastname = lname
    def printname(self):
        print(self.firstname,self.lastname)
#use the person class to create an object ,and execute the printname method:
x= Person("John","Doe")
x.printname()

#child class creation
class student(Person):
    pass
x=student("Mike","Olsen")
x.printname()