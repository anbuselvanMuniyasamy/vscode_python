import datetime  # Import datetime module to store transaction timestamps

# ----------------- BANK CLASS -----------------
# This class manages a single bank account for a user
class Bank:
    bank_name = "INDIAN OVERSEAS BANK"          # Class-level attribute: bank name
    branch = "9, Keelkattalai, Chennai"        # Class-level attribute: branch address

    # Constructor method to create a new account
    def __init__(self, username, pan, address, password):
        self.username = username                # Store user name
        self.pan = pan                          # Store PAN number
        self.address = address                  # Store address
        self.password = password                # Store password in plain text
        self.balance = 0.0                      # Initial account balance
        self.transactions = []                  # List to store transaction history
        print(f"Hello {username}, account created successfully!\n")

    # Method to verify password during login
    def verify_password(self, password):
        return self.password == password         # Return True if password matches

    # Method to deposit money
    def deposit(self, amount):
        if amount <= 0:                          # Check for valid amount
            print("Deposit must be > 0")
            return
        self.balance += amount                    # Increase account balance
        # Record the deposit transaction with date, type, and amount
        self.transactions.append({
            "type": "Deposit",
            "amount": amount,
            "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        print(f"{amount} deposited. Balance: {self.balance}\n")

    # Method to withdraw money
    def withdraw(self, amount):
        if amount <= 0:                          # Check for valid amount
            print("Withdraw must be > 0")
            return
        if amount > self.balance:                # Check for sufficient balance
            print("Insufficient balance")
        else:
            self.balance -= amount               # Reduce account balance
            # Record the withdrawal transaction
            self.transactions.append({
                "type": "Withdraw",
                "amount": amount,
                "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            print(f"{amount} withdrawn. Balance: {self.balance}\n")

    # Method to print account statement
    def statement(self):
        print(f"Account Holder: {self.username}")
        print(f"PAN: {self.pan}, Address: {self.address}, Balance: {self.balance}")
        print("Recent Transactions:")
        # Print last 5 transactions
        for txn in self.transactions[-5:]:
            print(f"{txn['date']} | {txn['type']} : {txn['amount']}")
        print("------------------------------------------------\n")


# ---------------- MAIN PROGRAM ----------------
accounts = {}  # Dictionary to store all accounts (account_no: Bank object)

while True:
    print("1. Create Account\n2. Login\n3. Exit")
    choice = input("Enter choice: ")           # User selects an option
    print("------------------------------------------------\n")
    
    # ----------------- CREATE ACCOUNT -----------------
    if choice == "1":
        username = input("Name: ")
        pan = input("PAN: ")
        address = input("Address: ")
        password = input("Set password: ")
        account_no = str(len(accounts) + 1001)  # Auto-generate account number
        # Create Bank object and store in accounts dictionary
        accounts[account_no] = Bank(username, pan, address, password)
        print(f"Account No: {account_no}\n")     # Show account number to user

    # ----------------- LOGIN -----------------
    elif choice == "2":
        acc_no = input("Account No: ")
        account = accounts.get(acc_no)           # Retrieve account object
        if account:
            password = input("Password: ")
            if account.verify_password(password):  # Check password
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
                    elif op == "4":                 # Logout option
                        break
                    else:
                        print("Invalid option")
            else:
                print("Incorrect password")
        else:
            print("Account not found")

    # ----------------- EXIT -----------------
    elif choice == "3":
        print("Thanks for using the bank!")
        break

    else:
        print("Invalid choice")
