class Employee:
    def __init__(self,name,id,days):
        self.name = name
        self.id = id
        self.days = days
        self.attend_days = 0
        self.totalDays = days
    
    def mark_attendance(self,value):
        if value == True:
            self.attend_days += 1
    
    def working_days(self):
        return self.days
    
    def attendanceReport(self):
        print()
        print(f"Name: {self.name}       |ID: {self.id}      |Attend Days: {self.attend_days}. | Working Days: {self.working_days()} ")
       
days = int(input("Enter the Days: "))
id = input("Enter the ID: ")
name = input("Enter the Name: ")
person = Employee(name,id,days)

for i in range(days):
    attend = input("Present:  Y or N: ")
    attend = attend.upper()
    if attend == 'Y':
        person.mark_attendance(True)

person.attendanceReport()

