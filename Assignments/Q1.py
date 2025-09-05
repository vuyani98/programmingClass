n = int(input("Enter a number: "))
sum_of_odds = sum(i for i in range(1, n + 1, 2))

print("The sum of odd numbers from 1 to", n, "is:", sum_of_odds)