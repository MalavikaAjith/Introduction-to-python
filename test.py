class Person:
    def __init__(self, name, age, std, branch):
        self.name = name
        self.age = age
        self.std = std
        self.branch = branch
p1 = Person("Ann",22 , 12, "science")
print(p1.name)
print(p1.age)
print(p1.std)
print(p1.branch)

print(' ')

class Person:
    def __init__(self, name, age, std, branch):
        self.name = name
        self.age = age
        self.std = std
        self.branch = branch
    def __str__(self):
        return f"{self.name}, {self.age}, {self.std}, {self.branch}"
p1 = Person("Ann", 22, 12, "science")
print(p1)

print(' ')

