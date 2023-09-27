a = 200
b = 30
if a > b:
    print(" a is greater than b")

a = 33
b = 33
if a > b:
    print(" a is greater than b")
elif a == b:
    print("a is equal to b")

a = 200
b = 30
if a < b:
    print("a is less than b")
elif a == b:
    print("a is equal to b")
else:
    print("a is greater than b")

a = 30
b = 200
if a > b:
    print("a is greater than b")
else:
    print("a is less than b")

if a < b: print("a is less than b")

print("A") if a > b else print("B")

print("A") if a > b else print("B") if a == b else print("C")

# using AND logical operator
a = 200
b = 30
c = 40
if a > b and a > c:
    print("Both conditions are true")

# using OR logical operator
if a > b or a < c:
    print("One of the condition is true")

# using not
a = 200
b = 30
if not a < b:
    print("a is not less than b")

# even number
a = 244
if a % 2 == 0:
    print("a is even number")

# odd number
b = 33
if b % 2 != 0:
    print("b is odd number")

# positive number
a = 10
if a > 0:
    print("a is a positive number")

# negative number
a = -10
if a < 0:
    print("a is a negative number")

Ann = 17
if Ann < 18 and Ann == 18:
    print("Ann is eligible to vote")
else:
    print("Ann is not eligible to vote")

a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
c = int(input("Enter 3rd number:"))
if a > b and a > c:
    print("a is greater")
elif b > a and b > c:
    print("b is greater")
else:
    print("c is greater")

