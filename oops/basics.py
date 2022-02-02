class Dog:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age
    def set_age(self, age):
        self.age = age

d = Dog("Tim", 12)
d.set_age(22)
print(d.get_age())



#d2 = Dog("Bill", 15)
#print(d2.get_name())
