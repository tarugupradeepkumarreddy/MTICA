class wolf:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def bark(self):
        print("grr...")
class Dog(wolf):
    def bark(self):
        print("wolf")
if __name__=="__main__":
    pet1=Dog("tomy","brown")
    pet1.bark()
    pet1.bark()
    print(pet1.name,"is of color",pet1.color)

##output
##wolf
##grr...
##wolf
