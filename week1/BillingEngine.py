class taxEngine:
    def __init__(self,amount,region):
        self.regions = {"America":0.10,"India":0.05,"Japan": 0.05 ,"China": 0.03}
        self.amount = amount
        self.region = region

    def taxCalculation(self):
        taxedValue = 0
        for key in self.regions:
            if key == self.region:
                taxedValue = self.regions[self.region] * self.amount
        return taxedValue
    
    def totalBill(self):
        totalBill = self.amount + self.taxCalculation()
        return totalBill
    

amount = int(input("Enter the amount: "))
region = input("Enter the region: ")
taxedAmout = taxEngine(amount,region)
print(taxedAmout.taxCalculation())
print(taxedAmout.totalBill())