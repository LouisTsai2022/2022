contents = open('textfiles/Plural.txt').readlines()
contents.pop(0)

for line in contents:
    line = line.strip('\n')
    value = line.split(" ")
    Q = value[0]
    text = value[1]

    if Q == "0":
        Q = "no"
    elif Q == "1":
        Q = "one"

    if Q != "one":
        if text[-1] in ['s', 'x', 'z']:
            text += 'es'
        elif text[-2:] in ['ch', 'sh']:
            text = text + 'es'
        elif text[-1] == '0' and text[-2:] not in ("aeiouy"):
            text = text + 'es'
        elif text[-1] == 'y':
            text = text[0:-1] + "ies"
        elif text[-2:] == "fe" and text[-3] != "f":
            text = text[:-2] + 'ves'
        elif text[-1] == "f" and text[-2] != "f":
            text = text[:-1] + "ves"
        else:
            text = text + 's'
        print(Q, text)
