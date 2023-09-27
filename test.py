student = {"Name": "Ann", "Place": "Kerala", "Age": 22, "RollNo.": 17}
print(student)

x = student["Age"]
print(x)

for x in student.keys():
    print(x)

for x in student.values():
    print(x)

student["Class"] = 12
print(student)

for x, y in student.items():
    print(x, y)

student["RollNO."] = 37
print(student)

student.pop("Class")
print(student)

student.copy()
print(student)