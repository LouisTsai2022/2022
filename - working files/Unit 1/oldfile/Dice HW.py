import random

rolls = int(input("How many rolls? "))
under = 0
craps = 0
over = 0
for i range(rolls):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    total = dice1 + dice2
    print(dice1, dice2)
    if total == 7:
        craps +=1
    elif total > 7:
        over += 1
    else:
        under += 1
