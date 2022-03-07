name = input("Enter name: ").upper()
while name != 'Quit':
    print(name)
    name = input("Enter name: ").upper()



n = int(input("Enter a number for factorial: "))
total = 1
i = 1
while i <= n:
    total = total * i
    i += 1
print(total)


n = int(input("Enter number: "))
while n != 1:
    print(n)
    if n % 2 == 0:
        n = int(n / 2)
    else:
        n = int(n * 3 + 1)
print(n)

