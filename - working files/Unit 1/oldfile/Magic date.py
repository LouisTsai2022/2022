year = input("Enter the year in dd/mm/yy format: ")

d = int(year[0:2])

m = int(year[3:5])

y = int(year[6:])

if d * m == y:
    print("This date is magic!")

else:
    print("This date is not magic!")
