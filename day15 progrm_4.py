class Vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
    def seating_capacity(self,capacity):
        return f"the seating capacity of  a{self.name} is {capacity} passengers"
class Bus(Vehicle):
    def seating_capacity(self,capacity=50):
        return super().seating_capacity(capacity=50)
school_bus=Bus("school Volvo",180,12)
print(school_bus.seating_capacity())
##output
##the seating capacity of  aschool Volvo is 50 passengers

