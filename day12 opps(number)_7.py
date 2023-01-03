class number:
    def __init__(self,n):
        self.n=n
    def checkEven(self):
        if self.n%2==0:
            return "Even"
        else:
            return"old"
       
    def calculateFactorial(self):
        if self.n==0:
            return 1
        res=1
        for i in range(1,self.n+1):
            res*=i
            return res
    def calculatesumDigits(self):
        if self.n<0:
            self.n=abs(self.n)
        temp=str(self.n)
        t=0
        for i in temp:
            t+=int(i)
        return t
    def checkArmstrongNumber(self):
        if self.n<0:
            self.n=abs(self.n)
        temp=str(self.n)
        t=0
        for i in temp:
            t+=int(i)**len(temp)
        if self.n==1:
            return'ArmstrongNumber'
        else:
           return' Not ArmstrongNumber'
    def checkprime(self):
        assert(self.n>=0),"not valid"
        if (self.n==1 or self.n==2 or self.n==3 ):
            return "prime"
        
        for i in range(2,self.n):
            if self.n%i==0:
                return "not prime"
            return "prime"
inp=int(input())
ob=number(inp)
print('Factorial of ',inp,'is',ob.calculateFactorial())
print(inp,"is",ob.checkEven())
print('sumDigits of ',inp, 'is',ob.calculatesumDigits())
try:
    print('\n'+str(inp), 'is',ob.checkArmstrongNumber())
except AssertionError as a:
    print(a)
try:
    p=ob.checkprime()
    print(p)
except AssertionError as ob:
    print(ob)



















        
##        temp=self.n*(self.n+1)
##        return temp
##    def calculateperimeter(self):
##        temp=2*(self.length+self.width)
##        return temp
##l=int(input())
##w=int(input())
##try:
##    ob=rectangle(l,w)
##    area=ob.calculatearea()
##    peri=ob.calculateperimeter()
##    print('area of rectangle ',area)
##    print('perimeter of rectangle ',peri)
##except AssertionError as a:
##    print(a)
##
##
##
##
##
##
##
##
##
##
##
##
##
##
####assert(length>=0 and width>=0),'Invalid'
