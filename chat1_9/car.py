class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_nmae = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_nmae.title()
    def read_odometer(self):
        print("this car has " + str(self.odometer_reading)+ " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles


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
