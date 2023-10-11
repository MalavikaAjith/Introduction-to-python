price = 50
a = "The price is {:.2f} dollars"
print(a.format(price))

print(' ')

quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

print(' ')

x = "I have a {carname}, it is a {model}."
print(x.format(carname = "Ford", model = "Mustang"))

x = "My name is {name}, I am {age} years old"
print(x.format(name = "Malavika", age = 22))