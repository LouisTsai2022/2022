letters = "ABCDE"
for i in range(len(letters)):
    letter = letters[i]
    line = ""
    for j in range(0, i+1):
        line += letter
    print(line)



for i in range(1,6): #loop for each line
    output = ""      #line string
    for j in range(1, i+1):
        output += str(i)
    print(output)



for i in range(1,6):
    line = ""
    for j in range(0,5-i):
        line += "."
    for k in range(0,i):
        line += str(i)
    print(line)
