import re
a = "My name is Malavika"
x = re.findall("^My.*Malavika$", a)
print(x)
x = re.search("^My.*Malavika$", a)
print(x)
x = re.findall("[a,m]", a)
print(x)
y = "That will be 45 dollars"
z = re.findall("\d", y)
print(z)
x = re.findall("n..e", a)
print(x)
x = re.findall("^My", a)
if x:
    print("Yes")
else:
    print("No")
x = re.findall("Malavika$", a)
if x:
    print("Yes")
else:
    print("No")
x = re.findall("M.*a", a)
print(x)
x = re.findall("M.+a", a)
print(x)
x = re.findall("na.?e", a)
print(x)
x = re.findall("n.{2}e", a)
print(x)