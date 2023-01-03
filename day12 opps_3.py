class stud:
    college='MTICA'
    course='MCA'
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def displaystud(self):
        print("name:"+self.name.title()+"\nroll.no :"\
              +str(self.rollno))
        print("college :"+self.college+"\ncourde:"+self.course)
lstobj=[]
for i in range(2):
    n=input()
    p=int(input())
    temp='obj'+str(i)
    temp=stud(n,p)
    lstobj.append(temp)
for i in lstobj:
    i.displaystud()
