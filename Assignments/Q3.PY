n = int(input("How many numbers do you want "))
numbers = []
for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers = numbers + [num]
print("initial numbers:", numbers)5
reversedNumbers = numbers[::-1]   # slicing method
print("Reversed Numbers:", reversedNumbers)
