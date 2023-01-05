class wolf:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def bark(self):
        print("grr...")
class Dog(wolf):
    def bark(self):
        print("wolf")
pet1=Dog("tomy","brown")
pet1.bark()
pet2=wolf("jimmy","grey")
pet2.bark()
Dog("abc","xyz").bark()

##output
##wolf
##grr...
##wolf
