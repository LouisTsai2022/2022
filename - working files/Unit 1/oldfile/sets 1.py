a = set('abcdddffaaefg')
print(type(a), a)
sentence = "Hello to the to my Hellp world the"
words = sentence.split()
set_words = set(words)
print(set_words)


if "Hello" in set_words:
    print("Found")
else:
    print("Not Found")

students_names = {()}
print(type(students_names))
