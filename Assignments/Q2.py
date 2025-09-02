n = int(input("Enter a number: "))

print("Multiplication Table for", n)
for i in range(1, 13):
    print(n, "x", i, "=", n * i)