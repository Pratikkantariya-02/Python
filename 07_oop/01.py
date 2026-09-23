class Car:
    def __init__(self,userbrand, usermodel):
        self.brand = userbrand
        self.model = usermodel

my_car = Car("BMW","M5")
print(my_car.brand)
print(my_car.model)

""" car is class and my_car is object of class car.
    __init__ is constructor of class car.
    self is a reference to the current instance of the class."""

# CLASS = Class is blue print use to create object.
# OBJECT = Object is represent data and behavior.
# CONSTRUCTOR = Is a specific method that is automaticallyb called when new object is created.