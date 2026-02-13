class electricBill:
    def __init__(self,houseId,unit):
        self.unit = unit
        self.cost  = 0
        self.houseId = houseId
    
    def bill_calculator(self):
        if self.unit > 0 and self.unit <= 100:
            self.cost = 5 * self.unit
        elif self.unit > 100 and self.unit <= 200:
            self.cost = 7 * self.unit
        elif self.cost > 200:
            self.cost = 10 * self.unit
        
        cost = self.cost
        return cost

    def bill_summary(self):
    
        print(f"Hoser ID: {self.houseId} |Units: {self.unit} | Bill Cost: {self.bill_calculator()}")

houseId = input("Enter the House ID: ")
units = int(input("Enter the units: "))
house = electricBill(houseId,units)
house.bill_summary()