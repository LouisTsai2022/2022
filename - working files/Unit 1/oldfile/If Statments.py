#age = int(input("Enter your age: "))

#if age >= 18:
#    print("You can buy alcohol")
#else:
#    print("You are not old enough to buy alcohol")

# vowels = 'aeiou'
# word = input('Please enter a word: ')
# last_letter = word[-1]
#
# if last_letter.lower() in vowels:
#     print("Your word ends in a vowel")
# else:
#     print("Your word ends in a consonant")


# mark = input("Enter your mark: ").strip()
# if mark.isdigit():
#     mark = int(mark)
#     if mark > 100:
#         print("That is not a valid grade")
#      else:
#         if mark > 80:
#           grade = 'A'
#         elif mark > 70:
#            grade = 'B'
#         elif mark > 50:
#             grade = 'C'
#         elif mark >30:
#              grade = 'D'
#         else:
#               grade = 'E'
#     print("Your grade is", grade)
# else:
#     print("Your grade is", grade)


# digits = input("Enter your number string").strip()
# if digits.isdigit():
#     total = 0
#     for d in digits:
#         total = total + int(d)
#     print(total)
# else:
#     print("Only enter numbers")


word = input("Enter a word").strip()

if len(word) % 2 == 0:
    # an even word
     print(word[0:len(word) // 2])
     print(word[len(word) // 2:])
else:
     print(word[len(word)//2])

password = input("Enter your new password").strip()
test_password = 0
valid_password = True

lc = False
uc = False
num = False
special = False

if len(password) < 6 or len(password) > 20:
    vaild_password = False
    print("Password must be at least 6 characters")

for character in password:
    if character.islower():
        lc = True
    if character.isupper():
        uc = True
    if character.isdigit():
        num = True
    if not character.isalnum():
        special = True

if lc == True:
    test_password += 1
if uc == True:
    test_password += 1
if num == True:
    test_password += 1
if special == True:
    test_password += 1

if valid_password == True and test_password >= 3:
    print("Your passed word has been accepted")
else:
    print("You need to include", 3 - tests_passed, "of the following")
    if lc == False:
        print("A lowercase letter")
    if uc == False:
        print("An uppercase letter")
    if num is False:
        print("A number")
    if special is False:
        print("A special character")


