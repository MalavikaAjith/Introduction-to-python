# unordered
a = {"apple", "banana", "cherry"}
print(a)

# duplicates not allowed
a = {"apple", "banana", "cherry", "apple"}
print(a)

a = {"apple", "banana", "cherry", True, 1, 2}
print(a)

# Add - add() method
a = {"apple", "banana", "cherry"}
a.add("orange")
print(a)

# update() method
a = {"apple", "banana", "cherry"}
b = {"pineapple", "mango", "papaya"}
a.update(b)
print(a)

# update() method - it can be any iterable object(tuples, list, dict etc)
a = {"apple", "banana", "cherry"}
b = ["kiwi", "orange"]
a.update(b)
print(a)

# Remove - remove()
a = {"apple", "banana", "cherry"}
a.remove("banana")
print(a)

# discard()
a = {"apple", "banana", "cherry"}
a.discard("banana")
print(a)

# pop()
a = {"apple", "banana", "cherry"}
a.pop()
print(a)

# clear()
a = {"apple", "banana", "cherry"}
a.clear()
print(a)

# loop
a = {"apple", "banana", "cherry"}
for x in a:
    print(x)

# union() method
a = {"a", "b", "c"}
b = {1, 2, 3}
c = a.union(b)
print(c)

# keep only the duplicates
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)
# OR
z = x.intersection(y)
print(z)

# keep all, but not the duplicates
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)
# OR
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)
