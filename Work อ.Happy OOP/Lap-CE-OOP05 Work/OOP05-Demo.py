class Person:
    def __init__(self, name):
        self.name = name
        self.friend = []
    
    def add_friend(self, person):
        self.friend.append(person)

John = Person('John')
Jane = Person('Jane')
John.add_friend(Jane)
print(John.friend[0].name)