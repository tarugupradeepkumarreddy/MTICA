class point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __del__ (self):
        class_name =self.__class__.__name__
        print(class_name,"destroyed")
##python shell
##output
##pt1=point()
##pt2=pt1
##pt3=pt1
##print(id(pt1),id(pt2),id(pt3))
##2524973629648 2524973629648 2524973629648
##del pt1
##del pt2
##del pt3
##point destroyed
##pt11=point(6,7)
##del pt11
##point destroyed
