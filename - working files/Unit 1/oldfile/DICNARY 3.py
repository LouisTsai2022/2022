# ask user to enter a sentence. Count the number of each word in the sentence.
# For example: The quick brown fox jumped over the lazy fox which was also brown due to the brown rain

words = {}
sentence = input("Enter Sentence: ")
word_list = sentence.split()
for word in word_list:
    word = word.lower()
    if word in words:
        words[word] += 1
    else:
        words[word] = 1
#     print(words)
# print(words)
for k, v in words.items():
    print(k, v)
# print(word_list)


