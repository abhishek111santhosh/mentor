class Rectangle:
    def __init__(self, length, breadth):
        """Initializes the dimensions of the rectangle."""
        self.length = length
        self.breadth = breadth

    def calculate_area(self):
        """Calculates and returns the area (Length * Breadth)."""
        area = self.length * self.breadth
        print(f"The Area of the Rectangle is: {area} sq units")
        return area

    def update_dimensions(self, new_length, new_breadth):
        """Updates both dimensions at once."""
        if new_length > 0 and new_breadth > 0:
            self.length = new_length
            self.breadth = new_breadth
            print(f"Dimensions updated to {self.length} x {self.breadth}")
        else:
            print("Dimensions must be positive numbers!")

# --- Testing the Class ---

# 1. Create a Rectangle object
rect = Rectangle(10, 5)

# 2. Calculate the initial area
rect.calculate_area()

# 3. Update the dimensions (making it larger)
rect.update_dimensions(15, 8)

# 4. Calculate the new area
rect.update_dimensions(15, 8)
rect.calculate_area()