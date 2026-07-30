class Car:
    total_car = 0

    def __init__(self,userbrand, usermodel):
        self.brand = userbrand
        self.model = usermodel
        Car.total_car += 1


class ElectricCar(Car):
    def __init__(self,userbrand,usermodel,battery_size):
        super().__init__(userbrand,usermodel)
        self.battery_size = battery_size


my_tesla = ElectricCar("Tesla","S","100kwh")

safari = Car("Tata","Safari")

print(Car.total_car)