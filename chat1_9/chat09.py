# class Dog():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def sit(self):
#         print(self.name.title()+"is now sitting.")
#     def roll_over(self):
#         print(self.name.title()+" rolled over! ")

# my_dog = Dog('while', 7)
# you_dog = Dog('black', 5)
# print("my dog's name is "+ my_dog.name.title())
# print("my dog is " + str(my_dog.age) + "years old")


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

my_tesla = ElectricCar('tesla', 'models', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# my_used_car = Car('subaru', 'outback', 2013)
# print(my_used_car.get_descriptive_name())

# my_used_car.update_odometer(235000)
# my_used_car.read_odometer()

# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()
# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())
# my_new_car.update_odometer(23)
# my_new_car.read_odometer()