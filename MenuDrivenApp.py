class app:
    def calculator(self,a,b):
        print("Operation: [1] + ,[2] - ,[3] /,[4] * ,[5] ** power")
        operation = int(input("Enter the operation number: "))
        if operation == 1:
            return a + b
        elif operation == 2:
            return a - b
        elif operation == 3:
            return a / b
        elif operation == 4:
            return a * b
        elif operation == 5:
            return a**b
        else:
            return ValueError("Value out of bound")
    
    def stringOperation(self,s1,s2):
        print("Operation: [1] + ,[2] * ,[3] length")
        operation = int(input("Enter the Operation: "))
        if operation == 1:
            return s1 + s2
        elif operation == 2:
            times = int(input("Enter the number of times: "))
            return [s1*times,s2*times]
        elif operation == 3:
            return[len(s1),len(s2)]
        
x = app()
print(x.calculator(10 ,12))
print(x.stringOperation("Hello","World"))