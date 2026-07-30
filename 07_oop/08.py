class Car:

    def __init__(self,userbrand, usermodel):
        self.__brand = userbrand
        self.__model = usermodel
    
    @staticmethod
    def general_description():
        return "Cars are means of transpot"

    @property
    def model(self):
        return self.__model


class ElectricCar(Car):
    def __init__(self,userbrand,usermodel,battery_size):
        super().__init__(userbrand,usermodel)
        self.battery_size = battery_size

my_car = Car("Tata","Safari")
# my_car.model = "City"
print(my_car.model)