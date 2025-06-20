class UsedCarLoan:
    def __init__(self, price, interest_rate, loan_term, loan_amount):

        self.loan_amount = price
        self.price = price
        self.interest_rate = interest_rate / 100  # แปลงเป็นทศนิยม
        self.loan_term = loan_term
    
    def calculate_monthly_payment(self):
        self.monthly_rate = self.interest_rate / 12  # อัตราดอกเบี้ยต่อเดือน
        self.num_payments = self.loan_term * 12  # จำนวนงวดทั้งหมด
        self.monthly_payment = (self.loan_amount * self.monthly_rate) / (1 - (1 + self.monthly_rate) ** -self.num_payments)

    def display_summary(self):
        print(f"ราคารถยนต์มือสอง: {self.loan_amount:,.2f} บาท")
        print(f"อัตราดอกเบี้ย: {self.interest_rate * 100:.2f}% ต่อปี")
        print(f"ระยะเวลาผ่อน: {self.loan_term} ปี")
        print(f"ค่าผ่อนรถยนต์รายเดือน: {self.monthly_payment:,.2f} บาท")

price = 5000000
loan_amount = price
interest_rate = 4.25
loan_term = 7
Mycar = UsedCarLoan(price, interest_rate, loan_term, loan_amount)
Mycar.calculate_monthly_payment()
Mycar.display_summary()