for x in range(0, 10, 2):
    print(x)

for x in range(1, 10, 2):
    print(x)

rows = int(input("Enter no.of rows:"))
for x in range(1, rows):
    for y in range(x):
        print("*", end=" ")
    print(" ")