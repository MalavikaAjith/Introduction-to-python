import re
a = "My name is Malavika"
x = re.findall("[arn]", a)
print(x)
if x:
    print("yes")
else:
    print("no")
x = re.findall("[a-n]", a)
print(x)
if x:
    print("yes")
else:
    print("no")
x = re.findall("[^arn]", a)
print(x)
if x:
    print("yes")
else:
    print("no")
x = re.findall("[0123]", a)
print(x)
if x:
    print("yes")
else:
    print("no")
x = re.findall("[0-9]", a)
print(x)
if x:
    print("yes")
else:
    print("no")
x = re.findall("[0-5][0-9]", a)
print(x)
if x:
    print("yes")
else:
    print("no")
x = re.findall("[a-zA-Z]", a)
print(x)
if x:
    print("yes")
else:
    print("no")
x = re.split("\s", a)
print(x)
x = re.split("\s", a, 1)
print(x)
x = re.sub("\s", "v", a)
print(x)
x = re.sub("\s", "v", a, 1)
print(x)
x = re.search(r"\bMa\w+", a)
print(x.span())
x = re.search(r"\bM\w+", a)
print(x.string)
x = re.search(r"\bM\w+", a)
print(x.group())