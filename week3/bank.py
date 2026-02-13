def start_atm():
    balance = 10000.0
    print("--- Welcome to the mental  Bank ---")
    print(f"Current Balance: ₹{balance}")

    while True:
        print("\n" + "="*30)
        print("1. Withdraw Money")
        print("2. Check Balance")
        print("3. Exit")
        
        choice = input("Select an option (1-3): ")

        if choice == '3':
            print("Thank you for banking with us. Have a great day!")
            break
        
        elif choice == '2':
            print(f"Your current balance is: ₹{balance}")

        elif choice == '1':
            try:
                raw_amount = input("Enter amount to withdraw: ")

                # 1. Handle non-numeric input (ValueError)
                if not raw_amount.replace('.', '', 1).isdigit():
                    raise ValueError("Transaction failed: Please enter a valid number, not text.")
                
                amount = float(raw_amount)

                # 2. Handle negative or zero amounts
                if amount <= 0:
                    raise ValueError("Transaction failed: Amount must be greater than zero.")

                # 3. Handle insufficient funds
                if amount > balance:
                    raise ArithmeticError(f"Transaction failed: Insufficient funds. (Balance: ₹{balance})")

                # If no exceptions were raised, update the balance
                balance -= amount
                print(f"✅ Success! You have withdrawn ₹{amount}")
                print(f"Updated Balance: ₹{balance}")

            except ValueError as ve:
                print(f"❌ Input Error: {ve}")
            except ArithmeticError as ae:
                print(f"❌ Balance Error: {ae}")
            except Exception as e:
                print(f"❌ An unexpected error occurred: {e}")
        
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    start_atm()