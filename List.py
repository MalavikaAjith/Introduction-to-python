# change list
a = ["apple", "banana", "cherry"]
a[1] = "blackcurrant"
print(a)

a = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
a[1:3] = ["blackcurrant", "watermelon"]
print(a)

# insert items
a = ["apple", "banana", "cherry"]
a.insert(2, "watermelon")
print(a)

# append items ( add items)
x = ["apple", "banana", "mango"]
x.append("orange")
print(x)

# extend items
a = ["apple", "banana", "cherry"]
b = ["mango", "pineapple", "papaya"]
a.extend(b)
print(a)

# add any iterable (can add any iterable object such as tuoles, set, dict etc)
a = ["apple", "banana", "cherry"]
b = ("mango", "pineapple", "papaya")
a.extend(b)
print(a)
