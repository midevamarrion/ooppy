# Create 3 files in the classes directory car.py, fruit.py, and bank.py. Define the following classes in each module respectively. 
# Car
# Fruit
# Account
# Each class should have one class attribute and three instance variables.
# class Car:
#     num_wheels = 4

#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

class Car:
    make="Macdezbenz"
    def __init__(self,color,model,speed):
        self.color=color
        self.model=model
        self.speed=speed
    def accelerate(self):
        return f"The acceleration of {self.model} is {self.speed}"
    def start_engine(self):
        return f"The engine of {self.make} is Single engine"
    def hired_car(self):
        return f"John hired {self.make} {self.model} of speed {self.speed}.Its colour is {self.color}"

