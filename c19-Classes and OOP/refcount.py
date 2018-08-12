import sys
print(sys.getrefcount(123))
a = 123
print(sys.getrefcount(123))
b = 123
print(sys.getrefcount(123))
c = 123
print(sys.getrefcount(123))
del(a)
print(sys.getrefcount(123))
c = 10
print(sys.getrefcount(123))

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

    def __del__(self):
        print("Destroyed")
