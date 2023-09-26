a = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(a)

a = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(a["brand"])

# Allow duplicates
a = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year" : 2020
}
print(a)

# get() method
a = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = a["model"]
print(x)

# get keys
x = a.keys()
print(x)

a = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
a["colour"] = "white"
print(a)

a = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = a.values()
print(x)

a = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = a.items()
print(x)

a = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
a["year"] = 2020
print(a)

a = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
a.update({"year": 2018})
print(a)

# remove
a = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
a.pop("model")
print(a)

a = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
a.popitem()
print(a)

a = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del a["model"]
print(a)

a = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
a.clear()
print(a)



