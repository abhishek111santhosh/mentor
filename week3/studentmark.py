def process_marks(filename):
    total_marks = 0
    valid_count = 0
    invalid_count = 0

    try:
        with open(filename, "r") as file:
            lines = file.readlines()

            # Check for empty file
            if not lines:
                print("Error: File is empty.")
                return

            print("Processing Data...")
            
            for line in lines:
                try:
                    # Strip whitespace and split by comma
                    data = line.strip().split(",")
                    
                    # check for format error (must be name,marks)
                    if len(data) != 2:
                        raise ValueError("Incorrect format")

                    name = data[0]
                    # Try converting marks to integer (handles 'abc' error)
                    marks = int(data[1])

                    # Print valid record
                    print(f"Student: {name}, Marks: {marks}")
                    
                    total_marks += marks
                    valid_count += 1

                except ValueError:
                    print(f"Skipping invalid record: {line.strip()}")
                    invalid_count += 1

            # Final Calculations
            if valid_count > 0:
                print(f"\nAverage Marks: {total_marks / valid_count}")
            else:
                print("\nNo valid marks to calculate average.")
            
            print(f"Valid Records: {valid_count}")
            print(f"Invalid Records: {invalid_count}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

# --- Run the Program ---
# create a dummy file first to test
with open("marks.txt", "w") as f:
    f.write("Rahul,80\nAnu,90\nArjun,abc\n,60")

process_marks("marks.txt")