lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))
for num in range(lower,upper+1):
    result = 0
    for i in range(1,num):
        if (num % i) == 0:
            result = result + i
    if num == result:
        print(num)

