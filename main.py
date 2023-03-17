# davaleba 1
class Rectangle:
    def __init__(self, width, length, color):
        self.width = width
        self.length = length
        self.color = color
    def perimeter(self):
        return  2 * (self.width + self.length)
    def area (self):
        return (self.width * self.length)
obj1 = Rectangle(5, 1, "blue")
print(obj1.width)
print(obj1.length)
print(obj1.color)
print(obj1.perimeter())
print(obj1.area())
obj2 = Rectangle(3, 3, "green")
print(obj2.width)
print(obj2.length)
print(obj2.color)
print(obj2.perimeter())
print(obj2.area())
obj3 = Rectangle(3, 7, "purple")
print(obj3.width)
print(obj3.length)
print(obj3.color)
print(obj3.perimeter())
print(obj3.area())

# davaleba 2
class Car:
    def __init__(self, brend, model, color):
        self.brend = brend
        self.model = model
        self.color = color
    def __str__(self):
        return f"manqnis brendia: {self.brend}, manqnis modelia: {self.model}, manqnis feria: {self.color}"
car1 = Car("ford", "mustang", "red")
print(car1.brend)
print(car1.model)
print(car1.color)
car2 = Car("toyota", "prius", "blue")
print(car2.brend)
print(car2.model)
print(car2.color)
car3 = Car("volkswagen", "golf", "green")
print(car3.brend)
print(car3.model)
print(car3.color)

# davaleba 3
class Dog:
    def __init__(self, breed, size, age, color):
        self.breed = breed
        self.size = size
        self.age = age
        self.color = color
    def sleep(self):
        return "dzagls dzinavs"
    def eat(self):
        return "dzagli wams"
    def run(self):
        return "dzagli darbis"
    def sit(self):
        return "dzagli zis"

dog1 = Dog("neapolitan mastiff", "large", "5 years", "black")
dog2 = Dog("maltese", "small", "2 years", "white")
dog3 = Dog("chow chow", "midium", "3 years", "brown")
print(dog1.sleep())
print(dog2.eat())
print(dog3.run())