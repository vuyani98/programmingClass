
#Parent class
class Animal:

    # Constructor
    def __init__(self, name, legs):
        self.name = name
        self.legs = legs

    def make_sound(self, sound):
        print(f"{self.name} says {sound}")
        


# inherits from animal class, a Child class
class Dog(Animal):

    #unique method for Dog class
    def fetch(self, item):
        print(f"{self.name} is fetching the {item}")


#inherits from animal class, a Child class
class Cat(Animal):

    def scratch(self):
        print(f"{self.name} is scratching!")




userAnimal = input("Choose an animal A for Dog and B for Cat: ").upper()
animalName = input("Enter the name of your animal: ")


if userAnimal == "A":
    userDog = Dog(animalName, 4)
    userDog.make_sound("Woof Woof")

elif userAnimal == "B":
    userCat = Cat(animalName, 4)
    userCat.make_sound("Meow Meow")
    
else:
    print("Invalid input")


