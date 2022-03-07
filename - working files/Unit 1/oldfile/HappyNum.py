Happy = 'False'

while Happy != True:

    for z in range(1, 999):
        total = 0

        current = z

        rem = z % 10

        total = total + (rem * 2)

        z = z // 10

        if z == 1:
            Happy = True

        if Happy:
            print(current, "Happy Number")

        else:
            print(current, "Unhappy Number")
