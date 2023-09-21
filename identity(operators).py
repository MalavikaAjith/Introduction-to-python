# is operator (Returns True if both variables are the same object)
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
print(x is y)
print(x == y)

# is not operator
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is not z)
print(x is not y)
print(x != y)