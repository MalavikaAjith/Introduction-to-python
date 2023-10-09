class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def func(self):
        print(self.firstname, self.lastname)
x = Person("Malavika", "Ajith")
x.func()
class student(Person):
    pass
x = student("Ann", "John")
x.func()

print(' ')

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def func(self):
        print(self.firstname, self.lastname)
class student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
x = student("Ann", "John")
x.func()

print(' ')

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def func(self):
        print(self.firstname, self.lastname)
class student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
x = student("Ann", "John")
x.func()

print(' ')

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def func(self):
        print(self.firstname, self.lastname)
class student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear = 2019
x = student("Ann", "John")
print(x.graduationyear)

print(' ')

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def func(self):
        print(self.firstname, self.lastname)
class student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
x = student("Ann", "John", 2019)
print(x.graduationyear)

