class Person:
    def __init__(self, fname, lname, age):
        self.firstname = fname
        self.lastname = lname
        self.age = age
    def func(self):
        print(self.firstname, self.lastname, self.age)
class Student(Person):
    def __init__(self, fname, lname, age):
        super().__init__(fname, lname, age)
    def myfunc(self):
        print("My name is", self.firstname , self.lastname, ", I am ", self.age, "years old.")
p1 = Student("Malavika", "Ajith", "22")
p1.myfunc()

print(" ")

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Drive!")
class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Sail!")
class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Fly!")
car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")
for x in (car1, boat1, plane1):
    x.move()

print(" ")

firstname = "Malavika"
lastname = "Ajith"
age = 22
details = "My name is {0} {1} and I am {2} years old"
print(details.format(firstname, lastname, age))

print(" ")

item = "orange"
price = 56
myorder = "Brought {0} for {1:.2f} rupees"
print(myorder.format(item, price))
