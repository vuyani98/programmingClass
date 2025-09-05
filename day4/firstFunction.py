#built in functions

# len()  abs()  round()  type()  str()  int()  float()  input()  print()

#built in modules

#math  random  datetime  os  sys  json
# in these built in functions there are many functions
#e.g in math.sqrt()  math.pow()  math.ceil()  math.floor()

# use the keyword def to define a function
def firstFunction():
    print("This is my first function")
    return 1


#function with parameters, i.e num1 and num2
def addTwoNumbers(num1, num2):
    sum = num1 + num2
    #print(f"The sum of {num1} and {num2} is: {sum}")
    return sum

firstNumber = int(input("Enter first number: "))
secondNumber = int(input("Enter second number: "))

result = addTwoNumbers(firstNumber, secondNumber) #calling function

print(f"The result is: {result}")