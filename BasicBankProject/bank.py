import datetime

# Bank class to manage a single user account
class Bank:
    bank_name = "INDIAN OVERSEAS BANK"
    branch = "9, Keelkattalai, Chennai"

    def __init__(self, username, pan, address, password):
        self.username = username
        self.pan = pan
        self.address = address
        self.password = password        # store user password
        self.balance = 0.0              # initial balance
        self.transactions = []          # store transaction history
        print(f"Hello {username}, account created successfully!\n")

    # Verify password when logging in
    def verify_password(self, password):
        return self.password == password

    # Deposit money and record transaction
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit must be > 0")
            return
        self.balance += amount
        self.transactions.append({"type":"Deposit","amount":amount,"date":datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
        print(f"{amount} deposited. Balance: {self.balance}\n")

    # Withdraw money and record transaction
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdraw must be > 0")
            return
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            self.transactions.append({"type":"Withdraw","amount":amount,"date":datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
            print(f"{amount} withdrawn. Balance: {self.balance}\n")

    # Print account statement
    def statement(self):
        print(f"Account Holder: {self.username}")
        print(f"PAN: {self.pan}, Address: {self.address}, Balance: {self.balance}")
        print("Recent Transactions:")
        for txn in self.transactions[-5:]:
            print(f"{txn['date']} | {txn['type']} : {txn['amount']}")
        print("------------------------------------------------\n")


# ---------------- MAIN PROGRAM ----------------
accounts = {}  # store all accounts

while True:
    print("1. Create Account\n2. Login\n3. Exit")
    choice = input("Enter choice: ")

    # Create Account
    if choice == "1":
        username = input("Name: ")
        pan = input("PAN: ")
        address = input("Address: ")
        password = input("Set password: ")
        account_no = str(len(accounts) + 1001)     # generate account number
        accounts[account_no] = Bank(username, pan, address, password)
        print(f"Account No: {account_no}\n")

    # Login
    elif choice == "2":
        acc_no = input("Account No: ")
        account = accounts.get(acc_no)
        if account:
            password = input("Password: ")
            if account.verify_password(password):
                while True:
                    print("1.Deposit 2.Withdraw 3.Statement 4.Logout")
                    op = input("Choice: ")
                    if op == "1":
                        amount = float(input("Deposit amount: "))
                        account.deposit(amount)
                    elif op == "2":
                        amount = float(input("Withdraw amount: "))
                        account.withdraw(amount)
                    elif op == "3":
                        account.statement()
                    elif op == "4":
                        break
                    else:
                        print("Invalid option")
            else:
                print("Incorrect password")
        else:
            print("Account not found")

    # Exit
    elif choice == "3":
        print("Thanks for using the bank!")
        break
    else:
        print("Invalid choice")
