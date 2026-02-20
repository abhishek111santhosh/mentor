class Employee:
    def __init__(self, name, employee_id, salary):
        """Initializes the employee's profile."""
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def increase_salary(self, amount):
        """Increases the salary by a specific amount."""
        if amount > 0:
            self.salary += amount
            print(f"Salary increased by: ${amount}")
        else:
            print("Increase amount must be positive.")

    def display_details(self):
        """Displays the employee's current information."""
        print("\n--- Employee Record ---")
        print(f"ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Current Salary: ${self.salary}")
        print("------------------------\n")

# --- Testing the Class ---

# 1. Create an Employee object
emp1 = Employee("Jordan Smith", "EMP-502", 65000)

# 2. Display initial details
emp1.display_details()

# 3. Apply a salary increase
emp1.increase_salary(5000)

# 4. Display details again to see the update
emp1.display_details()