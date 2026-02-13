class bank:
    def __init__(self,name,id,money):
        self.name = name
        self.id = id
        self.money = money

    def deposit(self,value):
        self.money = self.money + value

    def withdraw(self,value):
        self.money = self.money - value
    
    def check_balance(self):
        return self.money

name = input("Enter the name: ")
id = input("Enter your userId: ")
money = int(input("Enter the money: "))
person = bank(name,id,money)

instruction = None
limit = 0
while instruction != 1 or limit == 5:
    limit += 1
    print("Operation Bank: [1] quit, [2] deposit, [3] withdraw, [4] Bank Balance")
    instruction = int(input("Operation: "))
    if instruction == 1:
        print("Quit sucessful!")
    elif instruction == 2:
        value_d = int(input("Enter the deposit money: "))
        person.deposit(value_d)
    elif instruction == 3:
        value_w = int(input("Enter the withdrawing money: "))
        person.withdraw(value_w)
    elif instruction == 4:
        print(f"Balance: {person.check_balance()}")

