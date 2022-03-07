content = open('textfiles/Pangrams.txt').readlines()
content.pop(0)
alphabet = set(list('abcdefghijklmnopqrstuvwxyz'))
# print(alphabet)
for line in content:
    line = line.strip('\n')
    letters = set()
    for c in line:
        if c.isalpha():
            letters.add(c.lower())
    missing = alphabet.difference(letters)
    if len(missing) == 0:
        print(line)
        print("    ", "Pangram")
    else:
        print("    ", "It's Missing Not A Pangram")
