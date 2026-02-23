#Problem Statement:
#Create a project to process student marks and generate results.
#Functional Requirements:
#● Function to input marks

#● Function to calculate total and average
#● Function to assign grade
#● Function to display result
 
def input_marks():
    """
    Function to input marks for subjects.
    Returns a list of marks.
    """
    marks = []
    print("--- Enter Marks ---")
    # Let's assume there are 5 subjects, or we can ask the user
    try:
        num_subjects = int(input("How many subjects do you have? "))
        
        for i in range(num_subjects):
            mark = float(input(f"Enter marks for Subject {i+1}: "))
            marks.append(mark)
            
        return marks
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        return []

def calculate_stats(marks):
    """
    Function to calculate total and average.
    Returns a tuple (total, average).
    """
    if not marks:
        return 0, 0
    
    total = sum(marks)
    average = total / len(marks)
    return total, average

def assign_grade(average):
    """
    Function to assign grade based on average.
    Returns the grade as a string.
    """
    if average >= 90:
        return 'A+'
    elif average >= 80:
        return 'A'
    elif average >= 70:
        return 'B'
    elif average >= 60:
        return 'C'
    elif average >= 50:
        return 'D'
    else:
        return 'F (Fail)'

def display_result(marks, total, average, grade):
    """
    Function to display the final result.
    """
    print("\n" + "="*20)
    print("    STUDENT REPORT   ")
    print("="*20)
    print(f"Marks Obtained: {marks}")
    print(f"Total Score   : {total}")
    print(f"Average       : {average:.2f}")
    print("-" * 20)
    print(f"Final Grade   : {grade}")
    print("="*20)

# --- Main Program ---
if __name__ == "__main__":
    # 1. Call function to input marks
    student_marks = input_marks()
    
    if student_marks:
        # 2. Call function to calculate stats
        total_score, avg_score = calculate_stats(student_marks)
        
        # 3. Call function to assign grade
        final_grade = assign_grade(avg_score)
        
        # 4. Call function to display result
        display_result(student_marks, total_score, avg_score, final_grade)
 