# for every number 1 + 100 inc either print number or if multiple of 3 = "fi33"
#   5 = "bu33"
# 3+5 = "fi33bu33"

for x in range (1,101):
    if x % 3 == 0 and x % 5 != 0:
        print("fizz")
    elif x % 3 != 0 and x % 5 == 0:
        print("buzz")
    elif x % 3 == 0 and x % 5 == 0:
        print("fizzbuzz")
    else:
        print(x)
