#OOP

class Car: 
    #attributes
    #make, model, year, color
    #methods
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def start(self):
        print(f"The {self.color} {self.make} {self.model} is starting.")


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.car = None #initially no car


    def buy_car(self, car):
        self.car = car
        #print(f"{self.name} bought a {car.color} {car.make} {car.model}.")


glady = Person("Glady", 27)

mercedes = Car("Mercedes", "C300", 2021, "Black")
toyota = Car("Toyota", "Corolla", 2020, "White")
nissan = Car("Nissan", "Altima", 2019, "Blue")

glady.buy_car(mercedes)

print(f"{glady.name} owns a {glady.car.color} {glady.car.make} {glady.car.model}.")
