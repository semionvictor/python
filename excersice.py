class Vehicle():
    def __init__(self,brand,model,speed):
        self.brand = brand
        self.model = model
        self.speed = speed

    def move(self):
        print(f"The car is moving with a speed of {self.speed} km/h")
        self.__destroy()

    def __destroy(self):
        print(f"the car is filled")

class Car(Vehicle):
    def __init__(self,brand,model,speed,number_of_doors):
        print("this is a new car")
        super().__init__(brand,model,speed)
        self.numberOfDoors = number_of_doors

class Truck(Vehicle):
    def __init__(self, brand, model, speed,cargo_capacity):
        print("this vehicles is used for carrying heavy load")
        super().__init__(brand, model, speed)
        self().cargoCapacity = cargo_capacity


toyota = Car("toyota", 2025,"200", 4)
toyota.move()