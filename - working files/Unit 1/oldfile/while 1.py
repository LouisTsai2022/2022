x = 10
while x > 0:
    print(x)
    x = x - 1
print("Blast Off!")



n = int(input("Enter a number or -1 to exit: "))
while n > 0:
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")
    n = int(input("Enter a number or -1 to exit: "))
print("GoooooooooooodBye")



msg = "Hi"
i = 0
while i < len(msg):
    print(msg[i].upper())
    i += 1
