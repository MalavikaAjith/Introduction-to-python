import re
a = "My name is Malavika"
x = re.findall("\AMy", a)
print(x)
if x:
    print("Yes")
else:
    print("No")
x = re.findall("r\bain", a)
print(x)
if x:
    print("yes")
else:
    print("no")
x = re.findall("r\Bain", a)
print(x)
if x:
    print("yes")
else:
    print("no")
x = re.findall("\d", a)
print(x)
if x:
    print("yes")
else:
    print("no")
x = re.findall("\D", a)
print(x)
if x:
    print("yes")
else:
    print("no")
x = re.findall("\s", a)
print(x)
if x:
    print("yes")
else:
    print("no")
x = re.findall("\S", a)
print(x)
if x:
    print("yes")
else:
    print("no")
x = re.findall("\w", a)
print(x)
if x:
    print("yes")
else:
    print("no")
x = re.findall("\W", a)
print(x)
if x:
    print("yes")
else:
    print("no")
x = re.findall("Malavika\Z", a)
print(x)
if x:
    print("yes")
else:
    print("no")
