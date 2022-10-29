# create a super class - vehicles
# create two subclasses for 'vehicles' named car and bike
# define two methods in the 'vehicles' class named getspecs and displayspecs
# create a car or bike object and call methods

class Vehicles:
    def __init__(self):
        self.color = ""
        self.wheel_count = 0
        self.gear_type = ""

    def getspecs(self):
        self.color = input("Enter vehicle color: ")
        self.wheel_count = int(input("Enter wheel count: "))
        self.gear_type = input("Enter gear type: ")

    def displayspecs(self):
        print("Vehicle color:", self.color)
        print("Wheel count:", self.wheel_count)
        print("Gear type:", self.gear_type)

class Car(Vehicles):
    def __init__(self):
        self.seat_count = 0
        self.wheel_count = 4

    def car_getspecs(self):
        self.color = input("Enter car color: ")
        self.gear_type = input("Enter gear type: ")
        self.seat_count = input("Enter seat count: ")

    def car_displayspecs(self):
        print("Car color:", self.color)
        print("Wheel count:", self.wheel_count)
        print("Gear type:", self.gear_type)
        print("Seat count:", self.seat_count)

class Bike(Vehicles):
    def __init__(self):
        self.side_seat = True
        self.wheel_count = 2

    def getspecs(self):
        self.color = input("Enter bike color: ")
        self.gear_type = input("Enter gear type: ")
        self.side_seat = bool(input("Does it have side seat [1/0]: "))

    def displayspecs(self):
        print("Bike color:", self.color)
        print("Gear type:", self.gear_type)
        print("Has side seat:", self.side_seat)

swift = Car()
swift.getspecs()
swift.displayspecs()
swift.car_getspecs()
swift.car_displayspecs()
