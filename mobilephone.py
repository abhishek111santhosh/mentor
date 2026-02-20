class Mobile:
    def __init__(self, brand, model, price):
        """Initializes the phone's specifications and price."""
        self.brand = brand
        self.model = model
        self.price = price

    def apply_discount(self, discount_amount):
        """Reduces the price by a specific dollar amount."""
        if 0 < discount_amount < self.price:
            self.price -= discount_amount
            print(f"Success! Discount of ${discount_amount} applied.")
        else:
            print("Error: Invalid discount amount.")

    def display_mobile(self):
        """Prints the current details of the mobile device."""
        print("\n--- Mobile Specifications ---")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Current Price: ${self.price}")
        print("-----------------------------\n")

# --- Testing the Class ---

# 1. Create a Mobile object
my_phone = Mobile("FruitPhone", "Pro Max 15", 1200)

# 2. View initial details
my_phone.display_mobile()

# 3. Apply a discount (e.g., a Black Friday sale)
my_phone.apply_discount(150)

# 4. Show updated details
my_phone.display_mobile()