x = [8, 9, 10]
x[1] = 17
print(x)

print(' ')

y = [4, 5, 6]
x.extend(y)
print(x)

print(' ')

x.pop(0)
print(x)

print(' ')

x.sort()
print(x)

print(' ')

x *= 2
print(x)

print(' ')

x.insert(3, 25)
print(x)

print(' ')

x = int(input("Enter the number:"))
if x >= 0:
    print("Is a positive number")
else:
    print("Is a negative number")

print(' ')

rows = 6
for x in range(1, rows):
    for y in range(x):
        print("1", end=" ")
    print(' ')
