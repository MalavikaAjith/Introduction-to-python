a = {"Rose", "Orchid", "Dahlia", "Daisy", "Lily", "Jasmine", "Lotus"}
for x in a:
    print(x)

a.add("Sunflower")
print(a)

a.remove("Sunflower")
print(a)

b = {"Apple", "Banana", "Orange", "Rose", "Lotus"}

a.update(b)
print(a)

a = {"Rose", "Orchid", "Dahlia", "Daisy", "Lily", "Jasmine", "Lotus"}
b = {"Apple", "Banana", "Orange", "Rose", "Lotus"}
a.intersection_update(b)
print(a)

a = {"Rose", "Orchid", "Dahlia", "Daisy", "Lily", "Jasmine", "Lotus"}
b = {"Apple", "Banana", "Orange", "Rose", "Lotus"}
a.symmetric_difference_update(b)
print(a)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)

