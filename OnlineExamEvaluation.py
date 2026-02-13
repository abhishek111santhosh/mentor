class examEvaluation:
    def __init__(self,name,candidate_answer_list):
        self.name = name
        self.candidate_answer_list = candidate_answer_list
        self.answer_list = ['a','a','b','b','c','c','d','e','f','c']
        self.makrperAnswers = 10

    def validatemarks(self):
        correct = 0
        for i in range(len(self.answer_list)):
            if self.answer_list[i] == self.candidate_answer_list[i]:
                correct += 1
        
        return correct
    
    def calclculateScore(self):
        correct = self.validatemarks()
        score = self.makrperAnswers * correct
        return score
    
    def calculateGrade(self):
        score = self.calclculateScore()
        if score >= 90:
            return 'A'
        elif score >= 80 and score < 90:
            return 'B'
        elif score >= 70 and score < 80:
            return'C'
        elif score >= 60 and score < 70:
            return 'D'
        else:
            return 'Fail'

name = input("Enter the name: ")
candidate_answer  = ['a','c','b','b','d','c','f','e','f','c']
candidate = examEvaluation(name,candidate_answer)
print(f"Score: {candidate.calclculateScore()}")
print(f"Grade: {candidate.calculateGrade()}")