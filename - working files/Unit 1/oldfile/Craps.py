# ask the user for the number of rolls, 2 dice - 10 rolls
# number of rolls > 7
# craps = 7
# number of rolls < 7

import random

rolls = int(input("How many rolls? "))
under = 0
craps = 0
over = 0

for i in range(rolls):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    total = dice1 + dice2
    print(dice1, dice2)
    if total == 7:
        craps += 1
    elif total > 7:
        over += 1
    else:
        under += 1

print("*" * 10)
print("Under:", under)
print("Craps:", craps)
print("Over:", over)
