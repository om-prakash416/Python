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

print("*******************")
# access attributets
emp1 =Employee("manali",46566)
emp2 =Employee("maya",45566)
emp1.age=7
print(Employee.empCount)
emp1.displayEmployee()
print(hasattr(emp1,'age')) #return true if age attribute exist
print(getattr(emp1,'age')) #return value of 'age' attribute
print(setattr(emp1,'age',8)) #set attribute 'age' t 8


delattr(emp1,'age')
print(hasattr(emp1,'age'))

