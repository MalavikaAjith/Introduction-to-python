i = 1
while i < 6:
    print(i)
    i += 1

print(" ")

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

print(" ")

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

print(" ")

a = 1
while a < 6:
     print(a)
     a += 1
else:
    print("a is no less than 6")