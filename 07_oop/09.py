class Car:
    def __init__(self,userbrand, usermodel):
        self.brand = userbrand
        self.model = usermodel

class ElectricCar(Car):
    def __init__(self,userbrand,usermodel,battery_size):
        super().__init__(userbrand,usermodel)
        self.battery_size = battery_size

my_tesla = ElectricCar("Tesla","S","100kwh")
print(isinstance(my_tesla,Car))
print(isinstance(my_tesla,Car))