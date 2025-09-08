class BankAccount:

    def __init__(self, account_holder,balance=0, account_number=0):
        self.balance = balance
        self.account_number = account_number
        self.account_holder = account_holder

    
    #method opens a new bank account
    def open_account(self, name, initial_deposit):
        self.account_holder = name
        self.balance = initial_deposit
        self.account_number += 1

    # function / method is used to deposit money into the account
    def deposit(self, amount):
        self.balance += amount
        receipt = open("receipt.txt", "w")
        receipt.write(f"Deposit of ${amount} was successful, your new balance is ${self.balance}")
        receipt.close()
        return f"Your new balance is {self.balance}"
    
    # function / method is used to withdraw money from the account
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        else:
            self.balance -=  amount
            return f"Your withdrawal was successful, your new balance is {self.balance}"


print("To open a new bank account, please enter your name and initial deposit amount")
name = input("Enter your name: ")
initial_deposit = float(input("Enter your initial deposit amount: "))

#creating a new bank account object
new_account = BankAccount(name)

#opening a new bank account
new_account.open_account(name, initial_deposit)

print(f"Account successfully created for {new_account.account_holder} with account number ${new_account.account_number} and initial deposit of {new_account.balance}")

wantDeposit = input("Would you like to make a deposit: (yes/no)")

if wantDeposit.lower() == "yes":
    amount = float(input("Enter the amount to deposit: "))
    new_account.deposit(amount)
    print(f"{new_account.deposit(amount)} into your account")

    print("Do you want your receipt? (yes/no) ")
    wantReceipt = input()
    if wantReceipt.lower() == "yes":
        receipt = open("receipt.txt", "r")
        print(receipt.read())
        receipt.close()
        
else:
    print("Thank you for using our services")

