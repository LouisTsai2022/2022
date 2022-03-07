contents = open('textfiles/TriffidsCipher.txt').readlines()
contents.pop(0)
contents.pop(6)
list(str(contents))

for line in contents:
    value = line.split()
    x = value[0:]
    num = value[1:]
    if 'S' == '111':
        S = 111
    elif 'F' == '211':
        F = 211
    elif 'O' == '311':
        O = 311
    elif 'E' == '112':
        E = 112
    elif 'G' == '212':
        E = 212
    elif 'P' == '312':
        E = 312
    elif 'C' == '113':
        C = 113
    elif 'H' == '213':
        H = 213
    elif 'Q' == '313':
        Q = 313
    elif 'R' == '121':
        R = 121
    elif 'I' == '221':
        I = 221
    elif 'U' == '321':
        U = 321
    elif 'T' == '122':
        T = 122
    elif 'J' == '222':
        J = 222
    elif 'V' == '332':
        V = 332
    elif 'K' == '223':
        K = 223
    elif 'W' == '323':
        W = 323
    elif 'A' == '131':
        A = 131
    elif 'L' == '231':
        L = 231
    elif 'X' == '331':
        X = 331
    elif 'B' == '132':
        B = 132
    elif 'M' == '232':
        M = 232
    elif 'Y' == '332':
        Y = 332
    elif 'D' == '133':
        D = 133
    elif 'N' == '233':
        N = 233
    elif 'Z' == '333':
        Z = 333
    else:
         line = line + ""
    print(x, line)