class Base(object):
    #constructor
    def __init__(self,name):
        self.name=name
    # to get name
    def getName(self):
        return self.name

#inherited or sub class(note person in bracket)
class Child(Base):
    # constructor
    def __init__(self, name,age):
        Base.__init__(self,name)
        self.age = age
    #to get name
    def getAge(self):
       return self.age
   
#inherited or sub class (note person in bracket)
class GrandChild(Child):
    #constructor
    def __init__(self, name, age,address):
        Child.__init__(self,name,age)
        self.address = address
        
        #to get address
    def getAddress(self):
            return self.address

#Driver code
g = GrandChild("om1",23,"noida")
print(g.getName(),g.getAge(),g.getAddress())
       