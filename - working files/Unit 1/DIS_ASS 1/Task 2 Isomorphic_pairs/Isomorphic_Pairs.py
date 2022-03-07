contents = open('sample_date.txt').readlines()

for line in contents:
    line = line.strip("/")
    words = line.split(" ")
    pattern1 = ""
    pattern2 = ""
    first_word = words[0]
    second_word = words[1]

    if len(first_word) == len(second_word):
        for i in range(len(first_word)):
            j = i + 1
            found = False
            while j < len(first_word) and found == False:
                if first_word[i] == first_word[j]:
                    pattern1 += "+ " + str(j - i)
                    Found = True
                j += 1
            if found == False:
                pattern1 += "0"

        for i in range(len(second_word)):
            j = i + 1
            found = False
            while j < len(second_word) and found == False:
                if second_word[i] == second_word[j]:
                    pattern2 += "+ " + str(j - i)
                    found = True
                j += 1
            if found == False:
                pattern1 += "0"
        if pattern1 == pattern2:
            print('{} ISOMORPHS WITH REPETITION PATTERN')
        else:
            print('{} NOT ISOMORPHS')
    else:
        print('{} DIFFERENT LENGTHS')