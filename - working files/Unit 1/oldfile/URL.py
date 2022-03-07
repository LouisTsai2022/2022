content = open(text.txt).readlines()

for i in range(len(1, content)):
    URL = content(i).strip('\n')
    clean_url = ""
    j = 0
    while j < len(URL):
        charaeter = URL(j)
        if charaeter != '%':
            clean_url += charaeter
            j += 1
        else:
            marlin_values = URL[j + 1 : j + 3]
            M1 = marlin_values[0]
            M2 = marlin_values[1]
            if M1 != alpha
                value += hexvalue(M1) * 16
            else:
                value += M1
            print(M1)
            if M2 != alpha
                value += hexvalue(M2) * 16
            else:
                value += M2
            print(M2)

            new_chr = chr(value)
            clean_url += new_chr
            j += 3
    print(URL)
print(i)





