filename = "textfiles/results-1line.txt"
file = open(filename)
print(type(file))

contents = file.readlines()
print(type(contents))

nm_A = 0
nm_B = 0
nm_C = 0
nm_D = 0
nm_F = 0

for line in contents:
    line = line.strip("\n")
    value = line.split(", ")
    name = value[0]
    mark = int(value[1])
    if mark > 80:
        grade = 'A'
        nm_A += 1
    elif mark > 70:
        grade = 'B'
        nm_B += 1
    elif mark > 60:
        grade = 'C'
        nm_C += 1
    elif mark > 50:
        grade = 'D'
        nm_D += 1
    else:
        grade = 'F'
        nm_F += 1
    print(mark, name, grade)

print("SUMMARIZE")
print("A", nm_A)
print("B", nm_B)
print("C", nm_C)
print("D", nm_D)
print("F", nm_F)