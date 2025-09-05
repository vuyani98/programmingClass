
# import firstFunction
from firstFunction import addTwoNumbers

firstNumber = int(input("Enter first number: "))
secondNumber = int(input("Enter second number: "))

sum = addTwoNumbers(firstNumber, secondNumber) #calling function from another file

print(f"The sum of the two numbers is: {sum}")