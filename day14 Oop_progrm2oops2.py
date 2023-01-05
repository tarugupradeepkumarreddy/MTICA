class Employee:
    empCount=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empCount+=1
    def displayCount(self):
        print("Total Employee %d".format(Employee.empCount))
    def displayEmployee(self):
        print("Name :" ,self.name,",salary:",self.salary)
emp1=Employee("pradeep",5000)
emp1.displayEmployee()
print("is salary an attribute:",hasattr(emp1,'salary'))
print(getattr(emp1,'salary'))
setattr(emp1,'salary',7000)
print("Modified salary",getattr(emp1,'salary'))
print(hasattr(emp1,'desg'))
setattr(emp1,'desg','manager')
print("Added Attribute",getattr(emp1,'desg'))
delattr(emp1,'salary')
print(" is salary an Attribute:",hasattr(emp1,'salary'))

##OUTPUT
##Name : pradeep ,salary: 5000
##is salary an attribute: True
##5000
##Modified salary 7000
##False
##Added Attribute manager
## is salary an Attribute: False



