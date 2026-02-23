class costumer:
    def __init__(self):
        self.item = {'processor' : 0,'ram': 0,'rom': 0, 'cabin': 0}
        self.cost = 0
        self.Items = {'processor' : 200,'ram': 150,'rom': 300, 'cabin': 50}

    def addItems (self,value,quantity):
        if value == 1:

            self.item['processor'] += quantity
            print()
            print(f"Processor Added Succesflly :{quantity}")
            print()

        elif value == 2:

            self.item['ram'] += quantity
            print()
            print(f"ram Added Succesflly :{quantity}")
            print()

        if value == 3:

            self.item['rom'] += quantity
            print()
            print(f"rom Added Succesflly :{quantity}")
            print()
            
        if value == 4:
            self.item['cabin'] += quantity
            print()
            print(f"cabin Added Succesflly :{quantity}")
            print()

        else:
            ValueError("Invalid Input")
        

    def removeItems(self,value):
         if value == 1:
            
            self.cost -= self.Items['processor'] * self.item['processor']
            self.item['processor'] = 0
            print()
            print(f"Processor removed Succesflly!")
            print()

         elif value == 2:
            
            self.cost -= (self.Items['ram'] * self.item['ram'])
            self.item['ram'] = 0
            print()
            print(f"ram removed Succesflly!")
            print()


         if value == 3:
            
            self.cost -= self.Items['rom'] * self.item['rom']
            self.item['rom'] = 0
            print()
            print(f"rom removed Succesflly!")
            print()


         if value == 4:
            
            self.cost -= self.Items['cabin'] * self.item['cabin']
            self.item['cabin'] = 0
            print()
            print(f"cabin removed Succesflly!")
            print()


         else:
            ValueError("Invalid Input")

    def total_cost(self):
        for key  in self.Items:
            self.cost += self.Items[key] * self.item[key]
        return self.cost
        

    def discount(self,value):
        current_cost = self.total_cost()
        discounted = current_cost * (value/100)
        current_cost = current_cost - discounted
        return current_cost
    



print("Product List.")
print("____________________")
print("Product  |Cost. |No|")
print("Processor|200$. |1 |")
print("ram.     |150$. |2 |")
print("rom.     |300$. |3 |")
print("Cabin.   |50$.  |4 |")

person = costumer()
instruction = None
limit = 0
while instruction != 5 or limit == 5:
    limit += 1
    print("Operation Cart: [1] add Items, [2] remove Items, [3] print cost, [4] discounted price, [5] quit")
    instruction = int(input("Operation: "))
    if instruction == 1:

        product = int(input("Enter the product: "))
        quantity = int(input("Enter the quantity: "))
        person.addItems(product,quantity)
        
    elif instruction == 2:
        product = int(input("Enter the product: "))
        person.removeItems(product)
        
    elif instruction == 3:
        print(f"Cost: {person.total_cost()}")
        
    elif instruction == 4:
        discount = int(input("Enter the Discoutn: "))
        print(f"Discounted Price: {person.discount(discount)} ❤️")
        

    