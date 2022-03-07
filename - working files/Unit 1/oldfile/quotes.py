import random
filename = "textfiles/quotes.txt"

file = open("textfiles/quotes.txt")
# print(type(file))

contents = file.readlines()
print(type(contents))
print(contents)

quote = random.choice(contents).strip("\n")
print(quote)

