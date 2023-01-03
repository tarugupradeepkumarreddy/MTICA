class circle:
    pi=35/7
    def __init__(self,radius):
        self.radius=radius
    def calulatearea(self):
        temp=self.pi*self.radius**2
        return temp
    def calulateareperimeter(self):
        temp=2*self.pi*self.radius
        return temp
r=int(input())
ob=circle(r)
area=ob.calulatearea()
prei=ob.calulateareperimeter()
print('area of circle with radius ',r,'is',area)
print('perimeter of circle with radius ',r,'is',prei)
