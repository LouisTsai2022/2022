coded_msg = input("Enter Words: ")
clean_msg = ""
words = coded_msg.split("")
reversed(words)
for word in words:
    if word[0].upper():
        clean_msg = clean_msg + word + ""
    else:
