from car import Car

class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
    def describe_battery(self):
        print("this car has a  " + str(self.battery_size) + "-kwh battery")
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        
        message = "this car can go approximately " + str(range)
        message += " miles on a full change."
        print(message)

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        print("this car has a " + str(self.battery_size) + "-kwh battery")
    def fill_gas_tank():
        print("this car doesnt need a gas tank!")