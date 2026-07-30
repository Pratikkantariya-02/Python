class Car:
    def __init__(self,userbrand, usermodel):
        self.__brand = userbrand
        self.model = usermodel

    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.model}"

class ElectricCar(Car):
    def __init__(self,userbrand,usermodel,battery_size):
        super().__init__(userbrand,usermodel)
        self.battery_size = battery_size


my_tesla = ElectricCar("Tesla","S","100kwh")
print(my_tesla.get_brand())