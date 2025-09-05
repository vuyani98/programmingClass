import math

class Shape:

    # Initialize the shape with its properties, this is the constructor and should always be named __init__
    def __init__(self, sides, height=0, width=0, base=0, length=0):

        #these are attributes of a shape
        self.sides = sides
        self.height = height
        self.width = width
        self.length = length
        self.base = base

    #every function inside a class is called a method and should always have self as the first parameter
    def area(self):

        if self.shape_type == "Triangle":
            return 0.5 * self.base * self.height
        
        elif self.shape_type == "Square":
            return self.width * self.length
        
        else:
            return "Area calculation not available for this shape"


    def perimeter(self):
        pass

    
    def shape_type(self):

        if self.sides == 3:
            return "Triangle"
        elif self.sides == 4 and self.width == self.height:
            return "Square"
        elif self.sides == 5:
            return "Pentagon"
        elif self.sides == 6:
            return "Hexagon"
        else:
            return "Unknown Shape"
        


sides1 = int(input("Enter number of sides: "))

if sides1 == 3:
    height1 = int(input("Enter height: "))
    base1 = int(input("Enter base: "))
    userShape = Shape(sides1, height=height1, base=base1)

elif sides1 == 4:
    length1 = int(input("Enter length: "))
    width1 = int(input("Enter width: "))
    userShape = Shape(sides1, length=length1, width=width1)
    
    # userShape = Shape(sides1, lenght1, width1, base1, height1)

else:
    print("Shape not supported for area calculation")



print(f"You created a {userShape.shape_type()} with area: {userShape.area()}")