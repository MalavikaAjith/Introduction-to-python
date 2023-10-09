class MyClass:
    x = 5
p1 = MyClass()
print(p1.x)

print(' ')

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("Ann", 22)
print(p1.name)
print(p1.age)

print(' ')

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}, {self.age}"
p1 = Person("Ann", 22)
print(p1)

print(' ')

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def func(self):
        print("Hello my name is " + self.name)
p1 = Person("Ann", 22)
p1.func()

print(' ')

class Person:
    def __init__(myobject, name, age):
        myobject.name = name
        myobject.age = age
    def func(abc):
        print("Hello my name is " + abc.name)
p1 = Person("Ann", 22)
p1.func()

print(' ')

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("Ann", 22)
p1.age = 40
print(p1.age)

print(' ')

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("Ann", 22)
del p1.age
print(p1.age)
print(p1.name)

