class User:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Product:
    def __init__(self, user):
        self.user = user

# สร้างอินสแตนซ์ของ User โดยส่งค่าที่จำเป็น
user_instance = User("ProductName", 100)

# จากนั้นสร้างอินสแตนซ์ของ Product โดยส่ง user_instance เข้าไป
Ans1 = Product(user_instance)
