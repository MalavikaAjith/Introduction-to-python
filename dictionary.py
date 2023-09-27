# copy dictionary - copy()
a = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
b = a.copy()
print(b)

# OR dict()
a = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
b = dict(a)
print(b)

# 3 dictionaries
family = {"child1": {"name": "Emil", "year": 2004}, "child2": {"name": "Tobias", "year": 2007}, "child3": {"name": "Ann", "year": 2011}}
print(family)

# OR
child1 = {
  "name": "Emil",
  "year": 2004
}
child2 = {
  "name": "Tobias",
  "year": 2007
}
child3 = {
  "name": "Linus",
  "year": 2011
}

family = {
  "child1": child1,
  "child2": child2,
  "child3": child3
}
print(family["child2"]["name"])
