class BankAccount:
    def __init__(self, holder_name, account_number, balance):
        """Initializes the account with holder details and starting balance."""
        self.holder_name = holder_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        """Adds a specified amount to the balance."""
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited: ${amount}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        """Deducts money if the balance is sufficient."""
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Successfully withdrew: ${amount}")
        elif amount > self.balance:
            print("Insufficient funds!")
        else:
            print("Invalid withdrawal amount.")

    def display_balance(self):
        """Prints the current status of the account."""
        print("\n--- Account Details ---")
        print(f"Holder: {self.holder_name}")
        print(f"Account #: {self.account_number}")
        print(f"Current Balance: ${self.balance}")
        print("-----------------------\n")

# --- Creating an object and calling methods ---

# 1. Create an object
my_account = BankAccount("Alex Rivera", "88224400", 1000)

# 2. Display initial details
my_account.display_balance()

# 3. Perform a deposit
my_account.deposit(500)

# 4. Perform a withdrawal
my_account.withdraw(200)

# 5. Show final balance
my_account.display_balance()