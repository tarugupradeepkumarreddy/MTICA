class Employee:
    empCount=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empCount+=1
    def displayCount(self):
        print("Total Employee {0}".format(Employee.empCount))
    def displayEmployee(self):
        print("Name :" ,self.name,",salary:",self.salary)
emp1=Employee("pradeep",5000)
emp1.displayEmployee()
emp1.salary=17000
emp1.experience=3
emp1.displayEmployee()
emp1.name='kumar'
emp1.displayEmployee()
print(emp1.experience)

emp1.displayEmployee()
del emp1.salary

##OUTPUT
##Name : pradeep ,salary: 5000
##Name : pradeep ,salary: 17000
##Name : kumar ,salary: 17000
##3
##Name : kumar ,salary: 17000
