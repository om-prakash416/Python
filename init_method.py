# it is built init_ () function.
# the _init_method is similar to construction in c++ and java java .
# constructions are used to initializing the object's  state.
# like methods , a constructor also contains a collection of statements(io.e instructions) that are executed at the time of object creation.
# it runs as soom as an object of a class is instantiated.the method is useful to do any initialization you want to do with your object.

class Employee:
    # Common base class for all Employees
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name: ", self.name, ", Salary: ", self.salary)

# Creating Employee objects
emp1 = Employee("Manali", 40000)
emp2 = Employee("Maya", 50000)

# Printing the total number of employees
print("Total Employees:", Employee.empCount)

# Displaying employee details
emp1.displayEmployee()
emp2.displayEmployee()
