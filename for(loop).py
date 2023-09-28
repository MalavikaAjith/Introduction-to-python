a = ["apple", "banana", "cherry"]
for x in a:
    print(x)

for x in "banana":
    print(x)

# using break
a = ["apple", "banana", "cherry"]
for x in a:
    print(x)
    if x == "banana":
        break

a = ["apple", "banana", "cherry"]
for x in a:
     if x == "banana":
         break
     print(x)

a = ["apple", "banana", "cherry"]
for x in a:
    if x == "banana":
        continue
    print(x)

for x in range(6):
    print(x)

for x in range(2, 6):
    print(x)

for x in range(2, 30, 3):
    print(x)

for x in range(6):
    print(x)
else:
    print("Finally Finished")

for x in range(6):
    if x == 3:
        break
    print(x)
else:
    print("Finally Finished")

a = ["apple", "banana", "cherry"]
b = ["green", "yellow", "red"]
for x in a:
    for y in b:
        print(x, y)

for x in [1, 2, 3]:
    pass