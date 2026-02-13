class InsufficientFundsError(Exception):
    """Custom exception for when withdrawal exceeds balance."""
    pass

def atm_simulation():
    balance = 10000  # Initial Balance
    
    print("Welcome to the ATM!")
    print(f"Current Balance: ₹{balance}")

    while True:
        print("\n--------------------------------")
        user_input = input("Enter withdrawal amount (or type 'exit' to quit): ")

        # 1. Handle Exit condition
        if user_input.lower() == 'exit':
            print("Thank you for banking with us. Goodbye!")
            break

        try:
            # 2. Check for "Text instead of number"
            # If this conversion fails, Python automatically raises a ValueError
            try:
                amount = float(user_input)
            except ValueError:
                # We catch the system error and raise our own with a clearer message
                raise ValueError("Invalid input. Please enter a numeric value.")

            # 3. Check for "Negative or Zero"
            if amount <= 0:
                raise ValueError("Amount must be positive and greater than zero.")

            # 4. Check for "Amount > Balance"
            if amount > balance:
                # Using a custom exception (optional but professional) or standard ValueError
                raise InsufficientFundsError(f"Insufficient funds! You only have ₹{balance}.")

            # If we pass all checks, perform the transaction
            balance -= amount
            print(f"✔ Success! Withdrawn: ₹{amount}")
            print(f"  Remaining Balance: ₹{balance}")

        except InsufficientFundsError as e:
            print(f"⚠ Transaction Failed: {e}")
            
        except ValueError as e:
            print(f"⚠ Input Error: {e}")
            
        except Exception as e:
            print(f"⚠ An unexpected error occurred: {e}")

# Run the program
if __name__ == "__main__":
    atm_simulation()