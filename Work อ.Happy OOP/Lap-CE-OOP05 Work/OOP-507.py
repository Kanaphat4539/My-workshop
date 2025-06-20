class PersonalIncomeTax:
    def __init__(self, income, tax_amount):
        self.income = income
        self.money = income
        self.tax_amount = tax_amount
    
    def calculate_tax(self):
        if self.money <= 300000:
            self.tax_amount = self.money*0.05
            #print(f"ต้องจ่ายภาษี = {self.tax_amount} บาท")
        elif self.income <= 500000:
            self.tax_amount = self.money*0.10
            #print(f"ต้องจ่ายภาษี = {self.tax_amount} บาท")
        elif self.income <= 750000:
            self.tax_amount = self.money*0.15
            #print(f"ต้องจ่ายภาษี = {self.tax_amount} บาท")
        elif self.income <= 1000000:
            self.tax_amount = self.money*0.20
            #print(f"ต้องจ่ายภาษี = {self.tax_amount} บาท")
        elif self.income <= 2000000:
            self.tax_amount = self.money*0.25
            #print(f"ต้องจ่ายภาษี = {self.tax_amount} บาท")
        elif self.income <= 5000000:
            self.tax_amount = self.money*0.30
            #print(f"ต้องจ่ายภาษี = {self.tax_amount} บาท")
        else:
            self.income > 5000000
            self.tax_amount = self.money*0.35

        return self.tax_amount
    
    def display_summary(self):
        self.tax_amount = self.calculate_tax()
        print(f"รายได้: {self.income:,.2f} บาท")
        if self.money <= 150000:
            print(f"ไม่ต้องจ่ายภาษีครับ")
        else:
            print(f"ภาษีที่ต้องจ่าย: {self.tax_amount:,.2f} บาท")

income = 17500000  # รายได้ต่อปี
money = income
tax_calculator = PersonalIncomeTax(income, money)
tax_calculator.display_summary()

