def movie_booking_system():
    total_seats = 50

    print("🎬 Welcome to the Movie Ticket Booking System!")
    
    # Loop runs until all seats are gone
    while total_seats > 0:
        print(f"\n--------------------------------")
        print(f"💺 Seats Available: {total_seats}")
        
        try:
            user_input = input("Enter number of tickets to book: ")

            # 1. Validation: Check for text input
            # int() automatically raises a ValueError if input is text
            tickets = int(user_input)

            # 2. Validation: Check for negative or zero tickets
            if tickets <= 0:
                raise ValueError("You must book at least 1 ticket.")

            # 3. Validation: Check if enough seats are available
            if tickets > total_seats:
                # Requirement: Use raise Exception for this specific rule
                raise Exception(f"Sorry, only {total_seats} seats are left.")

            # If all checks pass, book the tickets
            total_seats -= tickets
            print(f"✅ Success! {tickets} tickets booked.")

        except ValueError as e:
            # Catches text input AND our custom negative number error
            print(f"⚠ Input Error: Please enter a valid positive number.")
            
        except Exception as e:
            # Catches our specific "not enough seats" error
            print(f"⚠ Booking Error: {e}")

    print("\n🚫 House Full! All tickets have been sold.")

# Run the system
movie_booking_system()