class Bank:
    def __init__(self, name, account_no, balance, password):
        self.name = name
        self.account_no = account_no
        self.balance = balance
        self.password = password
        self.transactions = []

    def authenticate(self, password):
        if self.password == password:
            return True
        else:
            return False

    def details(self, password):
        if not self.authenticate(password):
            print("Incorrect password. Cannot show details.")
            return
        print("Name:", self.name)
        print("Account Number:", self.account_no)
        print("Balance:", self.balance)
        print("Transaction History:")
        for t in self.transactions:
            print("-", t)

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited Rs.{amount}")
        print(f"Deposited Rs.{amount} successfully.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough balance.")
            self.transactions.append(f"Tried to withdraw Rs.{amount} but failed (low balance)")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrew Rs.{amount}")
            print(f"Withdrew Rs.{amount} successfully.")

    def calculate_interest(self, rate, time):
        interest = (self.balance * rate * time) / 100
        print(f"Interest on Rs.{self.balance} at {rate}% for {time} years is Rs.{interest}")
        return interest

# --- Using the class with multiple accounts ---

bank_accounts = []

# Creating two sample accounts
vishal = Bank("Vishal", 12345, 2000, "pass123")
Amit = Bank("Amit", 67890, 5000, "abc123")

# Add to the list
bank_accounts.append(vishal)
bank_accounts.append(Amit)

# Do some operations on Vishal's account
vishal.deposit(1500)
vishal.withdraw(1000)
vishal.calculate_interest(5, 2)
vishal.details("pass123")  # correct password
vishal.details("wrongpass")  # wrong password
