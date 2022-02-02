class Pet:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I dont know bruh")

class Cat(Pet):

    def __init__(self, name, age, color):
        super().__init__(name,age)
        self.color = color

    def speak(self):    
        print("Meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color} in color")

class Dog(Pet):

    def speak(self):
        print("Bark")

p = Pet("Tim", 19)
p.speak()
c = Cat("Jim", 15, "purple")
c.show()
d = Dog("Chim", 14)
d.speak()
