class Car:
    def __init__(self,userbrand, usermodel):
        self.brand = userbrand
        self.model = usermodel

my_car = Car("BMW","M5")
print(my_car.brand)
print(my_car.model)