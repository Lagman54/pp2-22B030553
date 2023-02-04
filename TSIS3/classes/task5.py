class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, money):
        self.balance += money

    def withdraw(self, money):
        if money <= self.balance:
            self.balance -= money
            print(f"You withdrew {money} tenge.\nYour balance: {self.balance}\n")
        else:
            print(f"Balance is not sufficient.\nYour balance: {self.balance}\n")


# account = Account("Aibar", 0)
# account.deposit(5000)
# account.withdraw(1000)
# account.withdraw(1000000000)
