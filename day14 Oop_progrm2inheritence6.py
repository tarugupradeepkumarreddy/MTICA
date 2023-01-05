class animal:
    def __init__(self,name,color):
        self.name=name
        self.color=color
class cat (animal):
    def mew(self):
        print("cat meows")
class Dog(animal):
    def bark(self):
        print("woof")
print(__name__)
pet1=Dog("tomy","brown")
pet2=cat("lucy","white")
pet1.bark()
pet2.mew()
print(pet1.name)
print(pet2.name)
##output
##__main__
##woof
##cat meows
##tomy
##lucy
