def a():
    print("Hello from a function")
a()

print(" ")

def a(fname):
    print(fname + " John")
a("Ann")
a("Rose")
a("Emily")

print(' ')

def a(fname, lname):
    print(fname + " " + lname)
a("Emily", "John")

print(' ')

def a(*kids):
    print("The youngest child is " + kids[2])
a("Emily", "John", "Ann")

print(' ')

def a(child1, child2, child3):
    print("The youngest child is " + child3)
a(child1="Emily", child2="John", child3="Ann")

print(' ')

def a(**kids):
    print("last name is " + kids["lname"])
a(fname = "Ann", lname = "John")

print(' ')

def a(country = "Norway"):
    print("I am from " + country)
a("India")
a()
a("UK")
a("Sweden")

print(' ')

def a(fruits):
  for x in fruits:
    print(x)

fruits = ["apple", "banana", "cherry"]

a(fruits)

print(" ")

def a(x):
    return 5 * x
print(a(3))
print(a(5))
print(a(9))

