i = 0
while i <= 20:
    print(i)
    i += 2

print(" ")

a = 1
while a <= 20:
    print(a)
    a += 2

print(" ")

i = 4
while i % 2 == 0:
    print("i is an even number")
    break
else:
    print("i is an odd number")

print(" ")

i = 1
while i <= 5:
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    print()
    i += 1

print(" ")

i = 1
while i <= 5:
    k = 1
    while k <= 5 - i:
        print('', end=" ")
        k += 1
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    print()
    i += 1

print(" ")

i = 5
while i >= 1:
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    print()
    i -= 1

print(" ")

i = 5
while i >= 1:
    j = 1
    while j <= i:
        print(j, end=" ")
        j += 1
    print()
    i -= 1

print(" ")

i = 1
while i <= 5:
    j = 1
    while j <= i:
        print(i, end=" ")
        j += 1
    print()
    i += 1

print(" ")

i = 1
while i <= 5:
    j = 1
    while j <= i:
        print(j, end=" ")
        j += 1
    print()
    i += 1