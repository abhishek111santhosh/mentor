#Problem Statement:
#Create a project to process student marks and generate results.
#Functional Requirements:
#● Function to input marks

#● Function to calculate total and average
#● Function to assign grade
#● Function to display result

class students:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def mark_average(self):
        mark_sum = 0
        for mark in self.marks:
            mark_sum += mark
        average = mark_sum/len(self.marks) 
        return average
    
    def grade(self):
        mark_dict = {'A': 0,'B': 0,'C': 0,'D': 0, 'Fail': 0}
        for mark in self.marks:
            if mark >= 90:
                mark_dict['A'] += 1
            elif mark < 90 and mark >= 80:
                mark_dict['B'] += 1
            elif mark < 80 and mark >= 70:
                mark_dict['C'] += 1
            elif mark < 70 and mark >= 60:
                mark_dict['D'] += 1
            elif mark < 60:
                mark_dict['Fail'] += 1
        return mark_dict
    
    def student_profile(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks[:]}")
        for key, grade in self.grade().items():
            print(f"Grade: {key}: {grade}")
        print(f"percentage mark {self.mark_average()}")

name = input("Enter the name: ")
mark_list = []
no_subjects = 6
for i in range(no_subjects):
    x = int(input(f"Enter the marks{i+1}: "))
    mark_list.append(x)

student = students(name,mark_list)
print()
student.student_profile()
    