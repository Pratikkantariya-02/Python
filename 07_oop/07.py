class Car:

    def __init__(self,userbrand, usermodel):
        self.brand = userbrand
        self.model = usermodel
    
    @staticmethod
    def general_description():
        return "Cars are means of transpot"


class ElectricCar(Car):
    def __init__(self,userbrand,usermodel,battery_size):
        super().__init__(userbrand,usermodel)
        self.battery_size = battery_size

my_car = Car("Tata","Safari")
print(Car.general_description())