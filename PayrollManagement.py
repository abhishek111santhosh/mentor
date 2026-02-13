class employee:
    def __init__(self,name,hours,department):
        self.name = name
        self.hours = hours
        self.department = department
        self.hourlypay = 500
        self.pay = 0

    def salary(self):
        salary = self.hours * self.hourlypay
        self.pay = salary
        return salary
    
    def bonus(self,percentage_value):
        salary = self.salary()
        bonus_percentage = salary * (percentage_value/100)
        bonus = salary + bonus_percentage
        self.pay = bonus
        return bonus
    
    def deduction(self,percentage_value):
        salary = self.salary()
        deduction_percentage = salary * (percentage_value/100)
        deduction = salary - deduction_percentage
        self.pay = deduction
        return deduction
    
    def payRoll(self):
        print(f"Name: {self.name}")
        print(f"Payroll Salary: {self.salary()}")
        print(f"Department: {self.department}")
        print(f"Hours: {self.hours}")

name = input("Enter the name: ")
hours = int(input("Enter the working hours: "))
department = input("Enter the Depatment: ")
person = employee(name,hours,department)
person.payRoll()
