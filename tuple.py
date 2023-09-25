# convert and change
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# convert and add
x = ("apple", "banana", "cherry")
y = list(x)
y.append("orange")
x = tuple(y)
print(x)

# OR
x = ("apple", "banana", "cherry")
y = ("orange",)
x += y
print(x)

# convert and remove
x = ("apple", "banana", "cherry")
y = list(x)
y.remove("apple")
x = tuple(y)
print(x)

# unpacking
x = ("apple", "banana", "cherry")
(green, yellow, red) = x
print(green)
print(yellow)
print(red)

x = ("apple", "banana", "cherry", "orange", "kiwi", "melon")
(green, yellow, *red) = x
print(green)
print(yellow)
print(red)