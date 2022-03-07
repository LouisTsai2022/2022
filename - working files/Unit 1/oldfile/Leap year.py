year = int(input("Enter a year: ").strip())

leap = False

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            leap = True
    else:
        leap = True

print("Result for", year, "=", leap)