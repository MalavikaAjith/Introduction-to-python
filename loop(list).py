# for loop
a = ["apple", "banana", "cherry"]
for x in a:
    print(x)

# using range() and len()
a = ["apple", "banana", "cherry"]
for i in range(len(a)):
    print(a[i])

# using while
a = ["apple", "banana", "cherry"]
i = 0
while i < len(a):
    print(a[i])
    i = i + 1

# short method for loop
a = ["apple", "banana", "cherry"]
[print(x) for x in a]
