class Base1(object):
    def __init__(self):
        self.str1 = "om1"
        print("base1")

class Base2(object):
    def __init__(self):
     self.str2 = "om2"
     print("Base2")
class Derived(Base1,Base2):
    def __init__(self):
      
        #calling constructors of Base2
        #and base2 classes
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived")
    def printStr(self):
       print(self)
       print(self.str1,self.str2)

ob = Derived()
ob.printStr()
     