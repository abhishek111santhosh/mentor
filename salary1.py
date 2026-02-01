class employees:
    def __init__(self,name,id,age,hour):
        self.name = name
        self.id = id
        self.age = age
        self.hour = hour
        self.hourlyRate = 500
        self.tax = 10
    def gross_salary(self):
        returnGrossSalary = self.hourlyRate * self.hour
        return returnGrossSalary
    
    def deduction(self):
        grossSalary = self.gross_salary()
        returnDeduction = (grossSalary * (self.tax/100)) 
        return returnDeduction

    def final_salary(self):

        grossSalary = self.gross_salary()
        deduction = self.deduction()
        finalSalary = grossSalary - deduction
        return finalSalary
    
    def employee_profile(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"ID: {self.id}")
        print(f"Gross Salary: {self.gross_salary()}")
        print(f"Deduction: {self.deduction()}")
        print(f"final Salary: {self.final_salary()}")
    
name = input("Enter the name: ")
id = int(input("Emplyer id number: "))
age = int(input("Enter the emplyee age: "))
hours = int(input("Enter the working hours: "))
employe = employees(name,id,age,hours)

employe.employee_profile()