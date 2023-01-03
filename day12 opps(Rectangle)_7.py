class rectangle:
    
    def __init__(self,length,width):
        assert(length>=0 and width>=0),'Invalid'
        self.length=length
        self.width=width
    def calculatearea(self):
        temp=self.length*self.width
        return temp
    def calculateperimeter(self):
        temp=2*(self.length+self.width)
        return temp
l=int(input())
w=int(input())
try:
    ob=rectangle(l,w)
    area=ob.calculatearea()
    peri=ob.calculateperimeter()
    print('area of rectangle ',area)
    print('perimeter of rectangle ',peri)
except AssertionError as a:
    print(a)
