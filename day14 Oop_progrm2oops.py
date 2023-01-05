class Employee:
    empCount=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empCount+=1
    def displayCount(self):
        print("Total Employee :",Employee.empCount)
    def displayEmployee(self):
        print("Name :" ,self.name,",salary:",self .salary)
emp1=Employee("pradeep",5000)
print("Total Employee",Employee.empCount)
emp2=Employee("kumar",2586)
emp1.displayEmployee()
emp2.displayEmployee()
print("total Employee {0}".format (Employee.empCount))
emp3=Employee("Manu Gupta",55585)
emp3.displayCount()
emp2.displayCount()
emp1.displayCount()
print("Total Employee {0}".format(Employee.empCount))

##OUTPUT
##Total Employee 1
##Name : pradeep ,salary: 5000
##Name : kumar ,salary: 2586
##total Employee 2
##Total Employee : 3
##Total Employee : 3
##Total Employee : 3
##Total Employee 3
