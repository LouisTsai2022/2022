n = int(input("How many numbers will you enter: "))

total = 0
average = 0
max = -1
min = 101
odd = 0
even = 0

for i in range(1, n + 1):
    num = int(input("Enter number" + str(i) + ": "))
    total += num
    if num > max:
        max = num
    if num < min:
        min = num
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

average = total / n
print("total:", total)
print("Average:", average)
print("Maximum:", max)
print("Minumum:", min)
print("Odd:", odd)
print("Even:", even)
