class Employee:
    """Common base class for all employees"""
    empCount = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name,  ", Salary: ", self.salary)


# This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
emp1.displayCount()
emp1.displayEmployee()
# This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
emp2.displayCount()
emp2.displayEmployee()


emp1.age = 7  # Add an 'age' attribute to the object emp1.
emp2.age = 8  # Modify 'age' attribute to the object emp1.
Employee.newvar = 10 # Add "newvar" class variable to Employee class

print(emp1.age, emp2.age, Employee.newvar)

del emp2.age  # Delete 'age' attribute from the object emp1.

print(emp1.age)
# print(emp2.age) # this will throw and error, since I've just deleted this attr
print(Employee.newvar)

########

print("hasattr : ", hasattr(emp1, 'age'))    # Returns true if 'age' attribute exists
print("getattr : ", getattr(emp1, 'age'))    # Returns value of 'age' attribute
print("setattr : ", setattr(emp1, 'age', 8))  # Set attribute 'age' at 8
print("delattr : ", delattr(emp1, 'age'))    # Delete attribute 'age'

########

emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee %d" % Employee.empCount)

########
print("Employee.__doc__:", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
print("Employee.__module__:", Employee.__module__)
print("Employee.__bases__:", Employee.__bases__)
print("Employee.__dict__:", Employee.__dict__)

########
## Destroying objects

a = 40      # Create object, ref count = 1
b = a       # Increase ref. count by one

del a       # Decrease ref. count to 1
b = 100     # Decrease ref. count to 0 (and now flagged for garbage collection)
