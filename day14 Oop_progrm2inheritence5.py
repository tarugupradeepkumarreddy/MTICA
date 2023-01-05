class A:
    def first_method(self):
        print("Mthod of class A...")
class B:
    def second_method(self):
        print("Method of class B...")
class C(B,A):
    def thrid_method(self):
        print("Method of class C...")
if __name__=='__main__':
    ob=C()
    ob.first_method()
    
    ob.thrid_method()
##    C().thrid_method()
##OUTPUT
##Mthod of class A...
##Method of class B...
##Method of class C...
