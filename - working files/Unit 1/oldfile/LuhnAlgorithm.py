contents = open('textfiles/LuhnAlgorithm.txt').readlines()
contents.pop(0)

card = input("Enter Credit Card Number: ")

card = [int(x) for x in card]

card = list(str(card))

check = card[-1]

del(card[-1])

card[0:2] = [2 * x, for x in card[0:2]]

for i, x in enumerate(card):
        card[i] = sum(map(int, str(x)))

card = sum(card) * 9

card = list(str(card))

card = [int(x) for x in card]

if card[-1] == check:
    print('Valid', card)
else:
    print('Encode', '')