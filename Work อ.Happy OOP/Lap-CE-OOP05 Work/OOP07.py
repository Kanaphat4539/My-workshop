class User:
    def __init__(self, Username):
        self.Username = Username
    def User_name(self):
        self.Username = self.Username
        print(f"ชื่อ คุณ:{self.Username}")

class Product:
    def __init__(self, Name, Price):
        self.name = Name
        self.price = Price
    def Shop(self):
        print(f"สินค้าชื่อ:{self.name} \nราคา:{self.price} บาท")

class Shopping:
    def __init__(self, user):
        self.user = user
        self.items = {}
        self.total = 0
    def Addproduct(self, product, quantity=1):
        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity
        self.total += product.price * quantity
        print(f'เพิ่มใสินค้าลงรถเข็น: {product.name} {quantity} ตัว \nราคารวม {self.total} บาท')
    def Buyproduct(self):
        print(f'{self.user.Username} สั่งซื้อ {self.total} บาท')


user1 = input("กรุณาใส่ชื่อ: ")
Name = User(user1)
Name.User_name()
Pro1 = Product('ลำโพงบลูทูธ',4000)
Pro2 = Product('Iphone 18 pro Max',96450)
Pro1.Shop()
Pro2.Shop()
product2 = Shopping(Name)
product2.Addproduct(Pro1,1)
product2.Addproduct(Pro2,1)
product2.Buyproduct()