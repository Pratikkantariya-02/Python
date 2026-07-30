class Car:
    def __init__(self,userbrand, usermodel):
        self.brand = userbrand
        self.model = usermodel

    def fuel_type(self):
        return "Petrol or Diesel"

class ElectricCar(Car):
    def __init__(self,userbrand,usermodel,battery_size):
        super().__init__(userbrand,usermodel)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"

my_tesla = ElectricCar("Tesla","S","100kwh")
print(my_tesla.fuel_type())

safari = Car("Tata","Safari")
print(safari.fuel_type())