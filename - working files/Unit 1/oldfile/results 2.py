filename = "textfiles/results.txt"
file = open(filename)
print(type(file))

contents = file.readlines()
print(type(contents))

names = []
mark = []
for i in range(len(contents +1)):
    if i % 2 != 0:
       names.append(contents[i])
    else:
        int.names.append(contents[i])
    print(names)
print(i)

for i in range(len(names)):
    name = names[i]
    mark = mark[i]


