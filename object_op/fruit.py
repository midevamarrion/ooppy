# Create 3 files in the classes directory car.py, fruit.py, and bank.py. Define the following classes in each module respectively. 
# Car
# Fruit
# Account
# Each class should have one class attribute and three instance variables.
# class Fruit:
#     is_healthy = True

#     def __init__(self, name, color, taste):
#         self.name = name
#         self.color = color
#         self.taste = taste
class Fruit:
    taste="sweet"
    def __init__(self,colour,price,name):
        self.colour=colour
        self.price=price
        self.name=name
    def buy_fruits(self):
        return f"I bought 4 {self.taste} {self.colour} {self.name} at {(self.price *4)}ksh"
    def make_juice(self):
        return f"i made {self.taste} {self.colour} juice from {self.name}"